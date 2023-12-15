/**
 * Function to style form inputs based on their 'required' attribute.
 *
 * Description:
 * This function selects all the input and textarea elements within a form with the id 'form-for-user'.
 * It then checks if each input element has the 'required' attribute. If it does, the background color is set to '#e3e3e3'.
 * If the input element does not have the 'required' attribute and its type is not 'submit', the background color is set to '#ffffff'.
 * Similarly, for each textarea element, if it has the 'required' attribute, the background color is set to '#e3e3e3'.
 * Otherwise, the background color is set to '#ffffff'.
 *
 * Example usage:
 * styleFormInputs();
 */

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
