<template>
  <scaffold-alert
    header-text="Shortcomings in Your Estimate"
    @back="
      state.marker = 'you_age1';
    "
    @next="
      state.marker = 'sho_ref1';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        Part of the scientific process is probing at potential weaknesses in your measurement, including the overall methods and execution. Try to identify some shortcomings in the approach this data story takes in the measurement of the age of the universe to this point or any difficulties you had with the process. (What are some reasons you or someone else might question your result?)
      </p>
      <v-textarea
        outlined
        auto-grow
        rows="2"
        label="Shortcoming #1"
      ></v-textarea>
      <v-textarea
        outlined
        auto-grow
        rows="2"
        label="Shortcoming #2"
      ></v-textarea>
      <v-textarea
        outlined
        auto-grow
        rows="2"
        label="Other Shortcomings"
        hint="(if you can think of any more)"
      ></v-textarea>
    </div>
  </scaffold-alert>
</template>
