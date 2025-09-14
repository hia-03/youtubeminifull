/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", // шаблоны в myapp/templates
    "./**/*.py",             // на случай, если классы пишешь в Python коде
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
