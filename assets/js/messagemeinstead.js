const emailLink = document.querySelector("#email-link");
emailLink.addEventListener("click", (event) => {
  event.preventDefault();
  const email = event.target.textContent.trim();
  navigator.clipboard.writeText(email);
  const message = `The email "${email}" has been copied to the clipboard. Sending a message is easier than email.`;
  window.alert(message);
});
