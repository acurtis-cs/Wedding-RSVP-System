
const noOne = document.getElementById("no_one");

const guestBoxes = document.querySelectorAll('input[name="guest"]');

noOne.addEventListener("change", function () {

    guestBoxes.forEach(function (box) {

        if (noOne.checked) {
            box.checked = false;
            box.disabled = true;
        } else {
            box.disabled = false;
        }

    });

});