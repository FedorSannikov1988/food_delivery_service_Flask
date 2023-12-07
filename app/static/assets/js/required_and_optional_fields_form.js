const form = document.getElementById('form-for-user');

const textareas = form.querySelectorAll('textarea');

const inputs = form.querySelectorAll('input');

inputs.forEach(input => {
  if (input.hasAttribute('required')) {
    input.style.backgroundColor = '#e3e3e3';
  } else {
    if (input.type !== 'submit') {
      input.style.backgroundColor = '#ffffff';
    }
  }
});

textareas.forEach(textarea => {
  if (textarea.hasAttribute('required')) {
    textarea.style.backgroundColor = '#e3e3e3';
  } else {
    textarea.style.backgroundColor = '#ffffff';
  }
});
