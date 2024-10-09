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

// Completed Data
const completedDataContainer = document.getElementById('completed-data');
managementData.completed.forEach((item) => {
  const completedOuterContainer = document.createElement('div');
  completedOuterContainer.classList.add(
    'w-40',
    'me-2',
    'mb-2',
    'p-2',
    'flex-grow-1',
  );
  completedOuterContainer.style.background = item.bg;

  const firstCompletedDiv = document.createElement('div');
  firstCompletedDiv.classList.add('d-flex', 'flex-row');

  const secondCompletedDiv = document.createElement('div');
  secondCompletedDiv.classList.add(
    'd-flex',
    'flex-row',
    'align-items-center',
    'justify-content-between',
  );

  const iconFirstContainer = document.createElement('span');
  iconFirstContainer.classList.add('me-2');
  iconFirstContainer.innerHTML = `<i class="fa-solid ${item.icon}"></i>`;
  iconFirstContainer.style.color = item.color;

  const titleFirstContainer = document.createElement('p');
  titleFirstContainer.textContent = item.name;
  titleFirstContainer.style.color = item.color;

  const countSecondContainer = document.createElement('h5');
  countSecondContainer.textContent = item.count;
  countSecondContainer.style.color = item.color;

  const sideContainer = document.createElement('div');
  sideContainer.classList.add('d-flex', 'flex-row', 'align-items-center');

  const iconSecondContainer = document.createElement('span');
  iconSecondContainer.classList.add('timer-icon', 'me-2');
  iconSecondContainer.innerHTML = `<i class="fa-regular fa-clock"></i>`;

  const timerSecondContainer = document.createElement('span');
  timerSecondContainer.textContent = item.time;
  timerSecondContainer.classList.add(`${item.timer}`);

  sideContainer.appendChild(iconSecondContainer);
  sideContainer.appendChild(timerSecondContainer);

  firstCompletedDiv.appendChild(iconFirstContainer);
  firstCompletedDiv.appendChild(titleFirstContainer);

  secondCompletedDiv.appendChild(countSecondContainer);
  secondCompletedDiv.appendChild(sideContainer);

  completedOuterContainer.appendChild(firstCompletedDiv);
  completedOuterContainer.appendChild(secondCompletedDiv);

  completedDataContainer.appendChild(completedOuterContainer);
});

const zoneContainer = document.getElementById('zone-data');
managementData.zonestats.zone_stats.forEach((item) => {
  const zoneDiv = document.createElement('div');
  zoneDiv.classList.add(
    'd-flex',
    'flex-row',
    'justify-content-between',
    'p-1',
    'mb-1',
    'zone-bg',
  );

  const iconEle = document.createElement('span');
  iconEle.innerHTML = `<i class="fa-solid ${item.icon}"></i>`;

  const titleEle = document.createElement('h6');
  titleEle.textContent = item.name;

  zoneDiv.appendChild(iconEle);
  zoneDiv.appendChild(titleEle);

  zoneContainer.appendChild(zoneDiv);
});

const greenContainer = document.getElementById('green-zone');
managementData.zonestats.green_zone.forEach((item, index) => {
  const greenDiv = document.createElement('div');
  greenDiv.classList.add(
    'd-flex',
    'flex-row',
    'justify-content-center',
    'align-items-center',
    'p-1',
    'mb-1',
    'green-bg',
  );

  const iconEle = document.createElement('span');
  iconEle.innerHTML = `<i class="fa-solid ${index < 3 ? '' : 'fa-clock'}"></i>`;

  const titleEle = document.createElement('h6');
  titleEle.classList.add('m-0', 'ms-2');
  if (item.color) {
    titleEle.classList.add(item.color);
  }
  titleEle.textContent = item.count;

  greenDiv.appendChild(iconEle);
  greenDiv.appendChild(titleEle);

  greenContainer.appendChild(greenDiv);
});

const yellowContainer = document.getElementById('yellow-zone');
managementData.zonestats.yellow_zone.forEach((item, index) => {
  const yellowDiv = document.createElement('div');
  yellowDiv.classList.add(
    'd-flex',
    'flex-row',
    'justify-content-center',
    'align-items-center',
    'p-1',
    'mb-1',
    'yellow-bg',
  );

  const iconEle = document.createElement('span');
  iconEle.innerHTML = `<i class="fa-solid ${index < 3 ? '' : 'fa-clock'}"></i>`;

  const titleEle = document.createElement('h6');
  titleEle.classList.add('m-0');
  if (item.color) {
    titleEle.classList.add(item.color);
  }
  titleEle.textContent = item.count;

  yellowDiv.appendChild(iconEle);
  yellowDiv.appendChild(titleEle);

  yellowContainer.appendChild(yellowDiv);
});

const redContainer = document.getElementById('red-zone');
managementData.zonestats.red_zone.forEach((item, index) => {
  const redDiv = document.createElement('div');
  redDiv.classList.add(
    'd-flex',
    'flex-row',
    'justify-content-center',
    'align-items-center',
    'p-1',
    'mb-1',
    'red-bg',
  );

  const iconEle = document.createElement('span');
  iconEle.innerHTML = `<i class="fa-solid ${index < 3 ? '' : 'fa-clock'}"></i>`;

  const titleEle = document.createElement('h6');
  titleEle.classList.add('m-0');
  if (item.color) {
    titleEle.classList.add(item.color);
  }
  titleEle.textContent = item.count;

  redDiv.appendChild(iconEle);
  redDiv.appendChild(titleEle);

  redContainer.appendChild(redDiv);
});
