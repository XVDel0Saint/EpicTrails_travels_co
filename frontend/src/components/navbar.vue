<template>
<!-- Navigation -->
<nav :class="['bg-dark text-white p-4 transition-all duration-200 shadow-md', { 'fixed top-0 left-0 right-0 z-50': isScrolled, '-translate-y-full': isHidden }]">
  <div class="container mx-auto flex justify-between items-center">
      <div class="text-2xl font-bold tracking-tight font-Poppins">EpicTrails</div>
      <div class="hidden md:flex space-x-6">
          <a v-for="item in navItems" :key="item" :href="`#${item.toLowerCase()}`" class="hover:text-yellow-300 transition duration-200">{{ item }}</a>

          <!-- Tooltip Wrapper for Desktop -->
          <div class="relative group">
              <!-- Book Now Button -->
              <button class="bg-yellow-600 text-white cursor-not-allowed font-Poppins font-semibold px-4 py-2 rounded-full hover:bg-yellow-500 transition duration-200 transform hover:scale-105">
                  Book Now
              </button>

              <!-- Tooltip message -->
              <span class="absolute left-full top-1/2 transform translate-y-1/3 -translate-x-24 mr-2 w-max px-3 py-1 text-sm text-white bg-gray-800 rounded opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                  Feature will be available soon
              </span>
          </div>
      </div>
      <button class="md:hidden text-white focus:outline-none" @click="toggleMobileMenu">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7" />
          </svg>
      </button>
  </div>
</nav>    

<!-- Mobile Menu -->
<div v-show="mobileMenuOpen" :class="['md:hidden bg-dark text-white transition-all ease-linear duration-300 shadow-lg overflow-hidden', { 'fixed left-0 right-0 z-40': isScrolled }]" :style="{ top: isScrolled ? '64px' : '0', maxHeight: mobileMenuOpen ? '300px' : '0' }">
  <div class="container text-center mx-auto px-4 py-2">
      <a v-motion-pop-visible-once v-for="item in navItems" :key="item" :href="`#${item.toLowerCase()}`" class="block py-2 hover:bg-white hover:text-black px-2 rounded transition duration-200" @click="toggleMobileMenu">{{ item }}</a>
      
      <!-- Tooltip Wrapper for Mobile -->
      <div class="relative group">
          <!-- Book Now Button for Mobile -->
          <button class="w-full font-Poppins font-semibold bg-yellow-600 text-white cursor-not-allowed px-4 py-2 rounded-full mt-2 hover:bg-yellow-500 transition duration-200">
              Book Now
          </button>

          <!-- Tooltip message for Mobile -->
          <span class="absolute left-full top-1/2 transform -translate-y-1/2 -translate-x-full mr-2 w-max px-3 py-1 text-sm text-white bg-gray-800 rounded opacity-0 group-hover:opacity-100 transition-opacity duration-200">
              Feature will be available soon
          </span>
      </div>
  </div>
</div>

</template>
  
<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'

const mobileMenuOpen = ref(false)
const isScrolled = ref(false)
const isHidden = ref(false)
let lastScrollPosition = 0

const toggleMobileMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value
}

const navItems = ['Home', 'About', 'Services', 'Testimonials', 'Contact']

const handleScroll = () => {
  const currentScrollPosition = window.pageYOffset || document.documentElement.scrollTop
  
  if (currentScrollPosition < 0) {
    return
  }
  isScrolled.value = currentScrollPosition > 5
  isHidden.value = currentScrollPosition > lastScrollPosition && currentScrollPosition > 5
  lastScrollPosition = currentScrollPosition
}


onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})

// Close mobile menu when scrolling
watch(isHidden, (newValue) => {
  if (newValue) {
    mobileMenuOpen.value = false
  }
})

</script>
