<template>

  <div class="relative min-h-screen w-full overflow-hidden bg-slate-50">

    <navbar/>

    <RouterView/>
  
    <mainfooter/>

  </div>
  
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
import navbar from './components/navbar.vue';
import mainfooter from './components/mainfooter.vue';

</script>