/*const mobileLink = document.querySelector("#mobile-link");
mobileLink.addEventListener("click", () => {
  const message = "The phone number is not available for your time zone. Please send a message instead.";
  window.alert(message);
});
*/


const phoneLink = document.querySelector("#mobile-link");
phoneLink.addEventListener("click", () => {
  const timeZone = Intl.DateTimeFormat().resolvedOptions().timeZone;
  if (timeZone === "Africa/Sao_Tome") {
    window.location.href = "tel:123-456-7890";
  } else {
    const message = "The phone number is not available for your time zone. Please send a message instead.";
    window.alert(message);
  }
});
