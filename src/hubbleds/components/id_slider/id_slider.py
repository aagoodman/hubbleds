from ipyvuetify import VuetifyTemplate
from echo.callback_container import CallbackContainer
from glue_jupyter.state_traitlets_helpers import GlueState
from numpy import where
from traitlets import observe, Float, Int, List, Unicode

from cosmicds.utils import load_template

class IDSlider(VuetifyTemplate):
    template = load_template("id_slider.vue", __file__,
                             traitlet=True).tag(sync=True)
    color = Unicode("#1E90FF").tag(sync=True)
    selected = Int(0).tag(sync=True)
    state = GlueState().tag(sync=True)
    step = Int(1).tag(sync=True)
    thumb_value = Float().tag(sync=True)
    tick_labels = List().tag(sync=True)
    vmax = Int(1).tag(sync=True)
    vmin = Int(0).tag(sync=True)
    
    def __init__(self, data, id_component, value_component, *args, **kwargs):
        # NB: We can't call this member value data
        # since VuetifyTemplate already has a data member
        # (that represents the typical Vue data)
        self.glue_data = data
        self.id_component = id_component
        self.value_component = value_component

        self._default_color = kwargs.get("default_color", "#1E90FF")
        self._highlight_ids = kwargs.get("highlight_ids", [])
        self._highlight_label = kwargs.get("highlight_label", None)
        self._highlight_color = kwargs.get("highlight_color", "orange")
        self.color = self._default_color

        self._id_change_cbs = CallbackContainer()

        self.refresh()
        self._selected_changed({"new": self.selected})

        if "step" in kwargs:
            self.step = int(kwargs["step"])
        super().__init__(*args, **kwargs)

    def update_data(self, data):
        self.glue_data = data
        self.refresh()

    def refresh(self):
        self.ids = sorted(self.glue_data[self.id_component], key=self._sort_key)
        self.values = sorted(self.glue_data[self.value_component])
        self.vmax = len(self.values) - 1
        self.selected_id = int(self.ids[self.selected])
        self.thumb_value = self.values[self.selected]
        self.tick_labels = ["Lowest"] + ["" for _ in range(self.vmax - 1)] + ["Highest"]

    def _sort_key(self, id):
        idx = where(self.glue_data[self.id_component] == id)[0][0]
        return self.glue_data[self.value_component][idx]

    def on_id_change(self, callback, run=True):
        self._id_change_cbs.append(callback)
        if run:
            callback(self.selected_id)

    def remove_on_id_change(self, callback):
        self._id_change_cbs.remove(callback)

    @observe('selected')
    def _selected_changed(self, change):

        old_index = change.get("old", None)
        index = change["new"]
        self.selected_id = int(self.ids[index])
        self.thumb_value = int(self.values[self.selected])
        highlighted = self.selected_id in self._highlight_ids
        old_highlighted = old_index is not None and self.ids[old_index] in self._highlight_ids

        if (highlighted or old_highlighted) and self._highlight_label is not None:
            labels = [x for x in self.tick_labels]
            if highlighted:
                labels[index] = self._highlight_label(self.selected_id)

            # Restore the end labels if we had previously changed them
            # and remove the highlighted label
            if old_index == 0:
                labels[0] = "Lowest"
            if old_index == len(self.ids) - 1:
                labels[-1] = "Highest"
            elif old_highlighted:
                labels[old_index] = ""
            self.tick_labels = labels

        if highlighted and self._highlight_color is not None:
            self.color = self._highlight_color
        elif self.color != self._default_color:
            self.color = self._default_color

        for cb in self._id_change_cbs:
            cb(self.selected_id)
    
