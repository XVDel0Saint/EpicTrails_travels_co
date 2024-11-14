/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {
      colors: {
        "primary":"#4C4B16",
        "secondary":"#898121",
        "accent":"#F87A53",

        "dark":"#000000",
        "night":"#0B192C",
      },
      fontFamily: {
        Roboto: ["Roboto, sans-serif"],
        Oswald: ["Oswald, sans-serif"],
        Poppins: ["Poppins, sans-serif"],
      },
      borderRadius: {
        'none': '0',
        'sm': '0.125rem',
        DEFAULT: '4px',
        'md': '0.375rem',
        'lg': '0.5rem',
        'full': '9999px',
        'large': '12px',
        '2xl': '21px',
        '3xl': '51px',
      },
      container:{
        padding: "2 rem",
        center: true,
      },
      //set breakpoints for screen sizes if necessary
    },
  },
  plugins: [],
}

