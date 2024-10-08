const icons = [
  'fa-magnifying-glass',
  'fa-filter',
  'fa-calculator',
  'fa-truck-medical',
  'fa-tv',
  'fa-stethoscope',
  'fa-tv',
  'fa-house-user',
  'fa-lock',
  'fa-globe',
  'fa-network-wired',
  'fa-circle-nodes',
  'fa-chart-column',
];

const sidebar = document.getElementById('sidebar');

// Dynamically create and append icon spans
icons.forEach((icon) => {
  const span = document.createElement('span');
  span.classList.add('text-white', 'mt-2', 'sidebar-icon');
  span.innerHTML = `<i class="fa-solid ${icon}"></i>`;
  sidebar.appendChild(span);
});
