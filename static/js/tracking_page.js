// JavaScript code for Tracking Page and Chart.js integration

// Example code for Chart.js integration
var ctx = document.getElementById('activity-chart').getContext('2d');
var myChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ['Category 1', 'Category 2', 'Category 3'],
    datasets: [{
      data: [12, 19, 8],
      backgroundColor: ['#7289da', '#5a68a2', '#4e5d94'],
      borderColor: '#fff',
      borderWidth: 1
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    legend: {
      position: 'bottom',
      labels: {
        fontColor: '#fff'
      }
    }
  }
});

// Example code for responsive form and component behavior
var form = document.getElementById('activity-form');
var editButtons = document.getElementsByClassName('edit-btn');
var deleteButtons = document.getElementsByClassName('delete-btn');

form.addEventListener('submit', function(event) {
  event.preventDefault();
  // Handle form submission
  var title = document.getElementById('title').value;
  var description = document.getElementById('description').value;
  var category = document.getElementById('category').value;
  var date = document.getElementById('date').value;
  var time = document.getElementById('time').value;
  var location = document.getElementById('location').value;
  var sustainabilityRating = document.getElementById('sustainability-rating').value;
  var notes = document.getElementById('notes').value;

  // Validate form data
  if (title && description && category && date && time && location && sustainabilityRating) {
    // Submit the form or perform desired action
    console.log('Activity logged:', title, description, category, date, time, location, sustainabilityRating, notes);

    // Clear form fields
    form.reset();
  } else {
    alert('Please fill in all required fields.');
  }
});

for (var i = 0; i < editButtons.length; i++) {
  editButtons[i].addEventListener('click', function(event) {
    var activityId = event.target.getAttribute('data-id');
    // Handle edit button click
    console.log('Edit activity:', activityId);
  });
}

for (var i = 0; i < deleteButtons.length; i++) {
  deleteButtons[i].addEventListener('click', function(event) {
    var activityId = event.target.getAttribute('data-id');
    // Handle delete button click
    console.log('Delete activity:', activityId);
  });
}

// Example code for navigation menu
var navItems = document.getElementsByClassName('nav-item');

for (var i = 0; i < navItems.length; i++) {
  navItems[i].addEventListener('click', function(event) {
    // Handle navigation menu click
    var target = event.target.getAttribute('data-target');
    console.log('Navigating to:', target);
  });
}

// Example code for scrolling behavior
var scrollButton = document.getElementById('scroll-top-btn');

scrollButton.addEventListener('click', function(event) {
  event.preventDefault();
  // Handle scroll to top button click
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
});

window.addEventListener('scroll', function() {
  // Show or hide scroll to top button based on scroll position
  if (window.pageYOffset > 100) {
    scrollButton.style.display = 'block';
  } else {
    scrollButton.style.display = 'none';
  }
});

// Example code for responsive menu
var menuToggle = document.getElementById('menu-toggle');
var menu = document.getElementById('menu');

menuToggle.addEventListener('click', function(event) {
  // Toggle menu visibility
  if (menu.style.display === 'none') {
    menu.style.display = 'block';
  } else {
    menu.style.display = 'none';
  }
});

window.addEventListener('resize', function() {
  // Hide menu on window resize if it is visible
  if (window.innerWidth > 768) {
    menu.style.display = 'none';
  }
});
