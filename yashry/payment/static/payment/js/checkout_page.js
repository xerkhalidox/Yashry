let governrates = ['Cairo', 'Alexandria', 'Luxor', 'Assiut', 'Giza'];
let cities = ['Nevada', 'Area 2', 'Area 51'];

let governrate_div = document.getElementById('governrate').lastElementChild;
let city_div = document.getElementById('city').lastElementChild;
let form = document.getElementById('form');
form.addEventListener('submit', is_locations_selected);
function is_locations_selected(e) {
  if (e.target[5].innerHTML.trim() == 'Governrate') {
    let alert_element = document.getElementsByClassName('alert');
    alert_element[0].hidden = false;
    alert_element[0].innerHTML = 'Please Select Your Fuckin Governrate';
    e.preventDefault();
  }
  if (e.target[6].innerHTML.trim() == 'City') {
    let alert_element = document.getElementsByClassName('alert');
    alert_element[0].hidden = false;
    alert_element[0].innerHTML = 'Please Select Your Fuckin City';
    e.preventDefault();
  }
}
function selected_item(e) {
  e.path[2].firstElementChild.innerHTML = e.target.innerHTML;
}
function appendChilds(parent, childs_array) {
  for (let index = 0; index < childs_array.length; index++) {
    let dropdown_item = document.createElement('span');
    dropdown_item.addEventListener('click', selected_item);
    dropdown_item.className = 'dropdown-item';
    dropdown_item.textContent = childs_array[index];
    dropdown_item.style.cursor = 'pointer';
    parent.appendChild(dropdown_item);
  }
}

appendChilds(governrate_div, governrates);
appendChilds(city_div, cities);
