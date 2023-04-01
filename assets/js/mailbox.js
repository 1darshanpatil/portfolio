const form = document.getElementById('myForm');
const submitBtn = document.getElementById('submit-btn');

form.addEventListener('submit', function(event) {
  event.preventDefault(); // prevent form from submitting

  // get form data
  const formData = new FormData(form);

  // build email message
  let message = `Hi Darshan,\n\n${formData.get('message')}\n\nBest Regards,\n${formData.get('name')}\n${formData.get('email')}` ;

  // encode message for email
  message = encodeURIComponent(message);

  // set email address and subject
  const email = 'drshnp@outlook.com';
  const subject = 'Contact Form Submission';

  // build mailto link
  const mailtoLink = `mailto:${email}?subject=${subject}&body=${message}`;

  // open email client
  window.location.href = mailtoLink;
});
