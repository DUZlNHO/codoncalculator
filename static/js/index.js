document.getElementById("dr").onchange = function () {
    document.getElementById("ct").setAttribute("disabled", "disabled");
    if (this.value == 'dna')
        document.getElementById("ct").removeAttribute("disabled");
    };
