import { icons } from './constants.js';

const sidebar = document.getElementById('sidebar');

icons.forEach((icon) => {
  const span = document.createElement('span');
  span.classList.add('text-white', 'sidebar-icon');
  span.innerHTML = `<i class="fa-solid ${icon}"></i>`;
  sidebar.appendChild(span);
});
