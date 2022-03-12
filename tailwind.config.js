// tailwind.config.js
module.exports = {
  content: [
    "./app/main/templates/*.{html,js}",
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
    styled: true,
    themes: ["dark", "emerald", "light", "cupcake", "bumblebee", "corporate", "synthwave", "retro", "cyberpunk", "valentine", "halloween", "garden", "forest", "aqua", "lofi", "pastel", "fantasy", "wireframe", "black", "luxury", "dracula", "cmyk", "autumn", "business", "acid", "lemonade", "night", "coffee", "winter"],
    base: true,
    utils: true,
    logs: true,
    rtl: false,
  },
};