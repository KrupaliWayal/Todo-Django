//  function changeColor(clickedDiv) {
//     clickedDiv.style.backgroundColor = 'green'; // Change the color of the clicked div to red
//   }

// safe todo.js - only affects the todo form
document.addEventListener('DOMContentLoaded', function () {
  const todoForm = document.getElementById('todoForm');
  if (!todoForm) return; // not on todo page -> do nothing

  // Example: basic handler (only prevent default if you do AJAX)
  todoForm.addEventListener('submit', function (e) {
    // If you intend to submit normally (server side), DO NOT prevent default.
    // If you want AJAX submission, uncomment the lines below and implement fetch().
    //
    // e.preventDefault();
    // const formData = new FormData(todoForm);
    // fetch(todoForm.action || window.location.pathname, {
    //   method: 'POST',
    //   body: formData,
    //   headers: { 'X-Requested-With': 'XMLHttpRequest' }
    // }).then(r => location.reload());

    // If you are not using AJAX, leave this handler empty (no preventDefault).
  });

  // Optional: scope any other todo-related handlers to page elements
  // e.g. click listeners for edit/delete buttons should be attached only when they exist:
  document.querySelectorAll('.Todo .fa-trash').forEach(btn => {
    btn.addEventListener('click', function (ev) {
      // handle delete if you use AJAX; otherwise normal link works.
    });
  });
});
