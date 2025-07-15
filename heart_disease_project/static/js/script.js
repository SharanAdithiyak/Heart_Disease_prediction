const form = document.querySelector("form"),
      nextBtn = form.querySelector(".nextBtn"),
      backBtn = form.querySelector(".backBtn"),
      allInput = form.querySelectorAll(".first input");

nextBtn.addEventListener("click", () => {
    let allFilled = true;

    allInput.forEach(input => {
        if (input.value.trim() === "") {
            allFilled = false;
        }
    });

    if (allFilled) {
        form.classList.add("secActive"); // Shows second section
    } else {
        alert("Please fill in all input fields.");
    }
});

backBtn.addEventListener("click", () => form.classList.remove("secActive")); // Returns to first

