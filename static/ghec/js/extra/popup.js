const modals = document.querySelector("#modals");
const openModals = document.querySelector(".open-buttons");
const closeModals = document.querySelector(".close-buttons");

openModals.addEventListener("click", () => {
  modals.showModal();
});

closeModals.addEventListener("click", () => {
  modals.close();
});
