<template>
  <scaffold-alert
    header-text="Age of the Universe"
    @back="
      state.marker = 'run_vel1';
    "
    @next="
      state.marker = 'hyp_gal1';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        As with the runners, you can use your galaxies’ velocity and distance data to calculate the time when all galaxies were in the same place — the <strong>age of the universe</strong>.
      </p>
      <p>
        To figure out the age of the universe implied by your whole dataset, we need to imagine a galaxy that is on the best fit line. Because your data may be messy, it is possible that none of your galaxies are on the best-fit line. (Click <strong>NEXT</strong> to make a galaxy appear on the line and in table “best fit galaxy”.)
      </p>
    </div>
  </scaffold-alert>
</template>
