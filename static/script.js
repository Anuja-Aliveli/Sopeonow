import { icons } from './constants.js';

// Parse the management_data from the script tag
const managementData = JSON.parse(
  document.getElementById('managementData').textContent,
);

console.log('managementData: ', managementData);

// Add icons to the sidebar dynamically

const sidebar = document.getElementById('sidebar');

icons.forEach((icon) => {
  const span = document.createElement('span');
  span.classList.add('text-white', 'sidebar-icon');
  span.innerHTML = `<i class="fa-solid ${icon}"></i>`;
  sidebar.appendChild(span);
});

// Add Key Metrics dynamically

const keyMetricsEle = document.getElementById('keyMetricsData');

managementData.key_metrics.forEach((item) => {
  // Outer div
  const outerDiv = document.createElement('div');
  outerDiv.classList.add('metric-container');
  outerDiv.classList.add('mt-1', 'div-border', 'p-1');

  // P element
  const pElement = document.createElement('p');
  pElement.textContent = item.caption;

  // Inner Div
  const innerDiv = document.createElement('div');
  innerDiv.classList.add('d-flex', 'flex-row', 'justify-content-between');

  // H4
  const h4Element = document.createElement('h4');
  h4Element.textContent = item.name;

  // div
  const timeIconContainer = document.createElement('div');
  timeIconContainer.classList.add(
    'w-25',
    'd-flex',
    'flex-row',
    'justify-content-start',
    'align-items-center',
  );

  // span for icon
  const iconElement = document.createElement('span');
  iconElement.classList.add('timer-icon', 'me-2');
  iconElement.innerHTML = `<i class="fa-regular fa-clock"></i>`;

  // span for time
  const timerElement = document.createElement('span');
  timerElement.textContent = item.time;
  timerElement.classList.add(`${item.time_color}`);

  timeIconContainer.appendChild(iconElement);
  timeIconContainer.appendChild(timerElement);

  innerDiv.appendChild(h4Element);
  innerDiv.appendChild(timeIconContainer);

  outerDiv.appendChild(pElement);
  outerDiv.appendChild(innerDiv);

  keyMetricsEle.appendChild(outerDiv);
});

// Total Visits
const totalCount = document.getElementById('totalVisits');
const registrationTime = document.getElementById('registrationTime');

totalCount.textContent = managementData.visits.count;
registrationTime.textContent = managementData.visits.time;
