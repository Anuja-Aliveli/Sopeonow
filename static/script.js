import { icons } from './constants.js';

// Parse the management_data from the script tag
const managementData = JSON.parse(
  document.getElementById('managementData').textContent,
);

console.log('managementData: ', managementData);

const sidebar = document.getElementById('sidebar');

// Add icons to the sidebar dynamically
icons.forEach((icon) => {
  const span = document.createElement('span');
  span.classList.add('text-white', 'sidebar-icon');
  span.innerHTML = `<i class="fa-solid ${icon}"></i>`;
  sidebar.appendChild(span);
});
