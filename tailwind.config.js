// tailwind.config.js
module.exports = {
  content: [
    "./app/main/static/**/**/*.{js,ts,jsx,tsx}",
    "./app/main/static/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'media', // or 'media' or 'class'
  //theme: {},
  variants: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography'),
    require("daisyui")
  ],
  daisyui: {
    logs: false,
    themes: false,
    // styled: false,
    // base: false,
    // utils: false,
    // rtl: false,
  },
  daisyui: {
    styled: true,
    themes: [
      'light',
      'forest',
      'cupcake',
      'synthwave',
      'emerald',

    ],
    base: true,
    utils: true,
    logs: true,
    rtl: false,
  },
};