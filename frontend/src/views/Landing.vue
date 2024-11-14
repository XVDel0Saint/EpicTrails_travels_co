<template>
<!-- Hero Section with Carousel -->
<header id="home" class="relative h-screen flex items-center overflow-hidden">
    <div v-for="(image, index) in carouselImages" :key="index" 
         class="absolute inset-0 bg-cover bg-center transition-opacity duration-1000"
         :style="{ backgroundImage: `url('${image}')`, opacity: currentImageIndex === index ? 1 : 0 }">
    </div>
    <div class="absolute inset-0 bg-black opacity-50"></div>
    <div class="relative container mx-auto px-4 text-center z-10">
        <h1 class="text-4xl md:text-6xl font-bold mb-4 text-white leading-tight" v-motion-slide-visible-once-bottom>
            Discover Your Next Adventure
        </h1>
        <p v-motion-slide-visible-once-bottom class="text-xl mb-8 text-gray-200 max-w-2xl mx-auto">
            Embark on unforgettable journeys to the world's most breathtaking destinations with EpicTrails
        </p>
        <button @click="openDestinationModal" v-motion-slide-visible-once-bottom class="bg-yellow-600 font-Poppins text-white px-8 py-3 rounded-full text-lg font-semibold hover:bg-yellow-500 transition duration-300 transform hover:scale-105 shadow-lg">
            Explore Destinations
        </button>
    </div>
</header>


<!-- Destination Modal -->
<div v-if="showDestinationModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
    <div class="bg-white rounded-lg p-8 max-w-4xl w-full max-h-[90vh] overflow-y-auto">
      <div class="flex justify-between items-center mb-6">
        <h2 class="text-3xl font-bold text-gray-800" v-motion-slide-visible-once-bottom>Explore Destinations</h2>
        <button v-motion-slide-visible-once-bottom @click="closeDestinationModal" class="text-gray-600 hover:text-gray-800">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>
      <div class="grid grid-cols-2 md:grid-cols-3 gap-6">
        <div v-motion-pop-visible-once v-for="destination in destinations" :key="destination.name" 
             @click="selectDestination(destination)"
             class="cursor-pointer group">
          <div class="relative overflow-hidden rounded-lg shadow-md">
            <img :src="destination.image" :alt="destination.name" class="w-full h-48 object-cover transition duration-300 transform group-hover:scale-110">
            <div class="absolute inset-0 bg-black bg-opacity-40 flex items-center justify-center opacity-0 group-hover:opacity-100 transition duration-300">
              <span class="text-white text-lg font-semibold">{{ destination.name }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
</div>


<!-- Search Bar -->
<div v-motion-slide-visible-once-bottom class="container mx-auto px-4 -mt-24 relative z-10">
  <div class="bg-white rounded-lg shadow-2xl p-6 md:p-8 relative group">
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6 opacity-50 pointer-events-none">
      <div v-for="field in searchFields" :key="field.name">
        <label :for="field.name" class="block text-sm font-medium text-gray-700 mb-1">{{ field.label }}</label>
        <input 
          :type="field.type" 
          :id="field.name" 
          :name="field.name" 
          :placeholder="field.placeholder"
          class="w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-200"
          disabled
        >
      </div>
      <div class="md:col-span-4">
        <button 
          class="w-full bg-blue-600 text-white p-3 rounded-md font-semibold transition duration-300 shadow-md cursor-not-allowed"
          disabled
        >
          Find Your Perfect Trip
        </button>
      </div>
    </div>
    <div 
      class="absolute inset-0 bg-gray-800 bg-opacity-75 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300 ease-in-out rounded-lg"
      role="tooltip"
      aria-hidden="true"
    >
      <p class="text-white text-center text-lg px-4 transform group-hover:scale-110 transition-transform duration-300 ease-in-out">
        Feature will be available soon, subscribe to our newsletter for updates
      </p>
    </div>
  </div>
</div>


<!-- About Section -->
<section id="about" class="py-20 bg-white relative">
    <div class="container mx-auto px-4">
    <h2 class="text-3xl md:text-4xl font-bold text-center mb-12 text-gray-800" v-motion-slide-visible-once-bottom>
        About EpicTrails
    </h2>
        <div class="max-w-4xl mx-auto">
            <p class="text-lg text-gray-600 mb-6 leading-relaxed" v-motion-slide-visible-once-bottom>
                At EpicTrails, we believe that every journey is a story waiting to be written. With over a decade of experience in crafting unforgettable adventures, we've made it our mission to turn your travel dreams into reality.
            </p>
            <p class="text-lg text-gray-600 mb-6 leading-relaxed" v-motion-slide-visible-once-bottom>
                Our team of passionate travel experts curates each experience with meticulous attention to detail, ensuring that every moment of your trip is filled with wonder, excitement, and authentic local encounters.
            </p>
            <p class="text-lg text-gray-600 leading-relaxed" v-motion-slide-visible-once-bottom>
                Whether you're seeking the serenity of pristine beaches, the thrill of mountain adventures, or the cultural richness of historic cities, EpicTrails is your gateway to extraordinary experiences that will stay with you for a lifetime.
            </p>
        </div>
    </div>
</section>


<!-- Services Section -->
<section id="services" class="py-20 bg-gray-100 relative">
    <div class="container mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-bold text-center mb-12 text-gray-800" v-motion-slide-visible-once-bottom >Our Services</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div v-for="service in visibleServices" :key="service.title" v-motion-slide-visible-once-bottom class="bg-white rounded-lg shadow-lg overflow-hidden">
                <img :src="service.image" :alt="service.title" class="w-full h-48 object-cover">
                <div class="p-6">
                    <div class="text-4xl text-yellow-500 mb-4">
                        <component :is="service.icon" />
                    </div>
                    <h3 class="text-xl font-semibold mb-2 text-gray-800">{{ service.title }}</h3>
                    <p class="text-gray-600">{{ service.description }}</p>
                </div>
            </div>
        </div>
        <div class="text-center mt-12">
            <button @click="toggleServices" v-motion-pop-visible-once class="bg-blue-600 font-Poppins text-white px-6 py-3 rounded-full text-lg font-semibold hover:bg-blue-700 transition duration-300 transform hover:scale-105 shadow-md">
            {{ showAllServices ? 'View Less' : 'View More' }}
            </button>
        </div>
    </div>
</section>


<!-- Fancy Blog Posts Section -->
<section class="py-20 bg-gray-100 relative overflow-hidden">
  <div class="container mx-auto px-4">
    <h2 class="text-4xl md:text-5xl font-bold text-center mb-16 text-gray-800">Travel Inspirations</h2>
    
    <!-- Blog Post 1 -->
    <article class="mb-20 bg-white rounded-2xl shadow-2xl overflow-hidden transform hover:scale-105 transition-all duration-300">
      <div class="md:flex">
        <div class="md:w-1/2">
          <img class="h-96 w-full object-cover" src="https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80" alt="Luxury beach resort">
        </div>
        <div class="md:w-1/2 p-8 md:p-12 flex flex-col justify-between">
          <div>
            <span class="text-blue-600 text-sm font-semibold tracking-wide uppercase">Luxury Getaways</span>
            <h3 class="mt-2 text-3xl font-bold text-gray-900 leading-tight">Discover Paradise: Top 5 Exotic Beach Resorts</h3>
            <p class="mt-4 text-gray-600 text-lg">Immerse yourself in ultimate luxury at these breathtaking coastal havens. From overwater bungalows to private beach villas, experience the epitome of relaxation and indulgence.</p>
          </div>
          <div class="mt-6 flex items-center">
            <img class="h-10 w-10 rounded-full mr-4" src="https://randomuser.me/api/portraits/women/32.jpg" alt="Author avatar">
            <div>
              <p class="text-sm font-semibold text-gray-900">Emma Rodriguez</p>
              <p class="text-sm text-gray-600">May 15, 2023 · 8 min read</p>
            </div>
          </div>
          <a href="#" class="mt-6 inline-block bg-gradient-to-r from-blue-500 to-teal-500 text-white px-6 py-3 rounded-full font-semibold hover:from-blue-600 hover:to-teal-600 transition duration-300 transform hover:scale-105">Read More</a>
        </div>
      </div>
    </article>

    <!-- Blog Post 2 -->
    <article class="bg-white rounded-2xl shadow-2xl overflow-hidden transform hover:scale-105 transition-all duration-300">
      <div class="md:flex flex-row-reverse">
        <div class="md:w-1/2">
          <img class="h-96 w-full object-cover" src="https://images.unsplash.com/photo-1533587851505-d119e13fa0d7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80" alt="Mountain hiking adventure">
        </div>
        <div class="md:w-1/2 p-8 md:p-12 flex flex-col justify-between">
          <div>
            <span class="text-green-600 text-sm font-semibold tracking-wide uppercase">Adventure Seekers</span>
            <h3 class="mt-2 text-3xl font-bold text-gray-900 leading-tight">Conquer the Heights: Epic Mountain Treks for Thrill-Seekers</h3>
            <p class="mt-4 text-gray-600 text-lg">Embark on adrenaline-pumping journeys through the world's most stunning mountain ranges. Our expert guides ensure unforgettable experiences for both novice hikers and seasoned trekkers.</p>
          </div>
          <div class="mt-6 flex items-center">
            <img class="h-10 w-10 rounded-full mr-4" src="https://randomuser.me/api/portraits/men/45.jpg" alt="Author avatar">
            <div>
              <p class="text-sm font-semibold text-gray-900">Alex Thompson</p>
              <p class="text-sm text-gray-600">May 20, 2023 · 10 min read</p>
            </div>
          </div>
          <a href="#" class="mt-6 inline-block bg-gradient-to-r from-teal-500 to-blue-500 text-white px-6 py-3 rounded-full font-semibold hover:from-teal-600 hover:to-blue-600 transition duration-300 transform hover:scale-105">Explore Adventures</a>
        </div>
      </div>
    </article>
  </div>
</section>


<!-- Testimonials Section -->
<section id="testimonials" class="py-20 bg-dark overflow-hidden relative">
    <div v-motion-pop-visible-once class="container mx-auto px-4">
        <h2 class="text-3xl md:text-4xl text-white font-bold text-center mb-12">What Our Travelers Say</h2>
        <div class="relative" @mouseenter="pauseTestimonials" @mouseleave="resumeTestimonials">
          <div class="flex transition-transform duration-500 ease-in-out" :style="{ transform: `translateX(-${currentTestimonial * 100}%)` }">
            <div v-for="testimonial in testimonials" :key="testimonial.name" class="w-full flex-shrink-0 px-4">
              <div class="bg-white p-6 rounded-lg shadow-md transform transition duration-300 hover:scale-105 mx-auto max-w-lg">
                <img :src="testimonial.avatar" :alt="testimonial.name" class="w-20 h-20 rounded-full mx-auto mb-4 border-4 border-yellow-500">
                <p class="mb-4 italic">"{{ testimonial.quote }}"</p>
                <div class="font-semibold">{{ testimonial.name }}</div>
                <div class="text-sm opacity-75">{{ testimonial.location }}</div>
              </div>
            </div>
          </div>
        </div>
        <div class="flex justify-center mt-8">
          <button v-for="(_, index) in testimonials" :key="index" @click="setTestimonial(index)" :class="['w-3 h-3 rounded-full mx-1', currentTestimonial === index ? 'bg-yellow-400' : 'bg-gray-500']"></button>
        </div>
    </div>
</section>

<!-- Contact Section -->
<section id="contact" class="py-20 bg-white relative">
    <div class="container mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-bold text-center mb-12 text-gray-800" v-motion-slide-visible-once-bottom>
            Contact Us
        </h2>
        <div class="max-w-lg mx-auto">
          <form @submit.prevent="submitForm" class="space-y-6">
            <div v-motion-slide-visible-once-bottom v-for="field in contactFields" :key="field.name">
              <label :for="field.name" class="block text-sm font-medium text-gray-700 mb-1">{{ field.label }}</label>
              <input v-if="field.type !== 'textarea'" :type="field.type" :id="field.name" :name="field.name"
                     class="w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-200">
              <textarea v-else :id="field.name" :name="field.name" rows="4"
                        class="w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition duration-200"></textarea>
            </div>
            <div v-motion-slide-visible-once-bottom class="flex items-center">
              <input type="checkbox" id="newsletter" v-model="subscribeNewsletter" class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded">
              <label for="newsletter" class="ml-2 block text-sm text-gray-900">
                Stay updated with our newsletter
              </label>
            </div>
            <button type="submit" v-motion-pop-visible-once class="w-full font-Poppins bg-blue-600 text-white p-3 rounded-md font-semibold hover:bg-blue-700 transition duration-300 transform hover:scale-105 shadow-md">
              Send Message
            </button>
          </form>
        </div>
    </div>
</section>


<!-- Newsletter Subscription Modal -->
<div v-if="showSubscriptionModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
  <div class="bg-white rounded-lg p-8 max-w-4xl w-full flex">
    <div class="flex-1 pr-8">
      <div class="text-center">
        <svg class="mx-auto h-12 w-12 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
        </svg>
        <h2 class="mt-4 text-2xl font-bold text-gray-900">Thank You for Subscribing!</h2>
        <p class="mt-2 text-gray-600">You've successfully subscribed to our newsletter. Stay tuned for exciting travel updates and exclusive offers!</p>
      </div>
      <div class="mt-6 text-center">
        <button @click="closeSubscriptionModal" class="bg-blue-600 text-white px-4 py-2 rounded-md font-semibold hover:bg-blue-700 transition duration-300">
          Close
        </button>
      </div>
    </div>
    <div class="flex-1">
      <img src="https://images.unsplash.com/photo-1524842495237-6abc737eae1f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8dHJhdmVsfGVufDB8fDB8fHww" alt="Newsletter subscription" class="w-full h-full object-cover rounded-lg">
    </div>
  </div>
</div>

</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import {sendEmail} from '@/services/emailService.js'


const searchFields = [
  { name: 'destination', label: 'Destination', type: 'text', placeholder: 'Where do you want to go?' },
  { name: 'checkIn', label: 'Check-in', type: 'date', placeholder: 'Check In Date' },
  { name: 'checkOut', label: 'Check-out', type: 'date', placeholder: 'Check Out Date' },
  { name: 'travelers', label: 'Travelers', type: 'number', placeholder: 'Number of travelers' }
]

const allServices = [
  {
    icon: 'svg',
    title: 'Customized Itineraries',
    description: 'Tailor-made travel plans designed to match your unique preferences and interests.',
    image: 'https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1121&q=80'
  },
  {
    icon: 'svg',
    title: 'Luxury Accommodations',
    description: 'Hand-picked, premium lodgings that offer comfort, style, and unforgettable experiences.',
    image: 'https://images.unsplash.com/photo-1566073771259-6a8506099945?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80'
  },
  {
    icon: 'svg',
    title: 'Expert Guides',
    description: 'Knowledgeable local guides who bring destinations to life with insider insights.',
    image: 'https://images.unsplash.com/photo-1516939884455-1445c8652f83?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1167&q=80'
  },
  {
    icon: 'svg',
    title: 'Adventure Activities',
    description: 'Thrilling experiences for adrenaline seekers, from mountain climbing to water sports.',
    image: 'https://images.unsplash.com/photo-1533692328991-08159ff19fca?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1074&q=80'
  },
  {
    icon: 'svg',
    title: 'Cultural Immersion',
    description: 'Authentic local experiences that connect you with the heart of each destination.',
    image: 'https://images.unsplash.com/photo-1523730205978-59fd1b2965e3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1159&q=80'
  },
  {
    icon: 'svg',
    title: '24/7 Travel Support',
    description: 'Round-the-clock assistance to ensure your journey is smooth and worry-free.',
    image: 'https://images.unsplash.com/photo-1534536281715-e28d76689b4d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80'
  }
]

const showAllServices = ref(false)
const visibleServices = computed(() => showAllServices.value ? allServices : allServices.slice(0, 3))

const toggleServices = () => {
  showAllServices.value = !showAllServices.value
}

const testimonials = [
  {
    quote: 'EpicTrails crafted the perfect honeymoon for us. Every detail was thoughtfully planned, creating memories we will cherish forever.',
    name: 'Emma & James',
    location: 'New York, USA',
    avatar: 'https://randomuser.me/api/portraits/women/65.jpg'
  },
  {
    quote: 'As a solo traveler, I felt safe and inspired throughout my journey. The experiences were authentic and the local guides were exceptional.',
    name: 'Mark Thompson',
    location: 'London, UK',
    avatar: 'https://randomuser.me/api/portraits/men/32.jpg'
  },
  {
    quote: 'Our family adventure was beyond our wildest dreams. The kids were engaged, we were relaxed, and the destinations were breathtaking.',
    name: 'The Chen Family',
    location: 'Sydney, Australia',
    avatar: 'https://randomuser.me/api/portraits/women/26.jpg'
  },
  {
    quote: 'The cultural immersion experiences provided by EpicTrails were truly eye-opening. I gained a deep appreciation for local traditions.',
    name: 'Sophia Rodriguez',
    location: 'Barcelona, Spain',
    avatar: 'https://randomuser.me/api/portraits/women/45.jpg'
  },
  {
    quote: 'The attention to detail in our luxury accommodations was impeccable. Each hotel felt like a destination in itself.',
    name: 'Alexander & Olivia',
    location: 'Paris, France',
    avatar: 'https://randomuser.me/api/portraits/men/22.jpg'
  }
]

const currentTestimonial = ref(0)
const testimonialInterval = ref(null)

const setTestimonial = (index) => {
  currentTestimonial.value = index
}

const startTestimonialRotation = () => {
  testimonialInterval.value = setInterval(() => {
    currentTestimonial.value = (currentTestimonial.value + 1) % testimonials.length
  }, 5000)
}

const pauseTestimonials = () => {
  clearInterval(testimonialInterval.value)
}

const resumeTestimonials = () => {
  startTestimonialRotation()
}

onMounted(() => {
  startTestimonialRotation()
})

onUnmounted(() => {
  clearInterval(testimonialInterval.value)
})

const contactFields = [
  { name: 'name', label: 'Name', type: 'text' },
  { name: 'email', label: 'Email', type: 'email' },
  { name: 'message', label: 'Message', type: 'textarea' }
]

const subscribeNewsletter = ref(false)
const showSubscriptionModal = ref(false)

const submitForm = async () => {
  // Email sending
  const formData = {
    name: document.getElementById('name').value,
    email: document.getElementById('email').value,
    message: document.getElementById('message').value,
    subscribeNewsletter: subscribeNewsletter.value
  }

  //console.log('Form submitted with data:', formData)
  
  if (subscribeNewsletter.value) {
    //console.log('Subscribing email to newsletter:', formData.email)
    showSubscriptionModal.value = true
  }

  try {
    const response = await sendEmail(formData);
    if (response.status === 200){
        //console.log('email sent:', response)
    } else{
        //console.error("Failed to send mail:", response)
    }
  } catch (error) {
    //console.error("Something went wrong:", error)
  }

  // Reset form fields and checkbox
  document.getElementById('name').value = ''
  document.getElementById('email').value = ''
  document.getElementById('message').value = ''
  subscribeNewsletter.value = false

}

const closeSubscriptionModal = () => {
  showSubscriptionModal.value = false
}

// Hero Image Carousel
const carouselImages = [
  'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2073&q=80',
  'https://images.unsplash.com/photo-1493246507139-91e8fad9978e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80',
  'https://images.unsplash.com/photo-1518548419970-58e3b4079ab2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80',
  'https://images.unsplash.com/photo-1501785888041-af3ef285b470?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80'
]

const currentImageIndex = ref(0)
const carouselInterval = ref(null)

const startImageCarousel = () => {
  carouselInterval.value = setInterval(() => {
    currentImageIndex.value = (currentImageIndex.value + 1) % carouselImages.length
  }, 5000)
}

// Destination Modal
const showDestinationModal = ref(false)
const destinations = [
  { name: 'Tokyo, Japan', image: 'https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1194&q=80' },
  { name: 'Okinawa, Japan', image: 'https://images.unsplash.com/photo-1542640244-7e672d6cef4e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80' },
  { name: 'Paris, France', image: 'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2073&q=80' },
  { name: 'New York, USA', image: 'https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80' },
  { name: 'Bali, Indonesia', image: 'https://images.unsplash.com/photo-1537996194471-e657df975ab4?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1938&q=80' },
  { name: 'Santorini, Greece', image: 'https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2072&q=80' }
]

const openDestinationModal = () => {
  showDestinationModal.value = true
}

const closeDestinationModal = () => {
  showDestinationModal.value = false
}

const selectDestination = (destination) => {
  carouselImages[0] = destination.image
  currentImageIndex.value = 0
  closeDestinationModal()
}

</script>