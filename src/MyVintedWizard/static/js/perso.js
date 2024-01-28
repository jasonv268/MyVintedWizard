function changerCouleur(element) {
    element.classList.remove('bg-danger');
    element.style.backgroundColor = "#bdc3c7"
    setTimeout(function() {
        element.classList.add('bg-danger');
    }, 2000); // 2000 millisecondes (2 secondes)
}

function openModal(url) {
    // Ouvrir une fenêtre modale
    window.open(url, '_blank', 'height=600,width=800,resizable=no,scrollbars=yes');
    return false; // Empêcher le comportement par défaut du lien
}

$(document).ready(function () {
    $('#table').DataTable({})
})

