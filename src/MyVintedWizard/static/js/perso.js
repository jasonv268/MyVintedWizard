function changerCouleur(element) {

    var cardBody = element.querySelector('.svg-div');

    var span = document.createElement('span');
        span.className = 'spinner-border spinner-border-sm';
        span.setAttribute('role', 'status');
        span.setAttribute('aria-hidden', 'true');


    var svgContainer = element.querySelector('.svg-container');
    svgContainer.style.display = 'none';
    cardBody.appendChild(span);

    setTimeout(function() {
        var spinner = element.querySelector('.spinner-border');
        spinner.parentNode.removeChild(spinner);
        svgContainer.style.display = 'block';

    }, 2000); // 2000 millisecondes (2 secondes)
}

function openModal(url) {
    // Ouvrir une fenêtre modale
    window.open(url, '_blank', 'height=600,width=800,resizable=no,scrollbars=yes');
    return false; // Empêcher le comportement par défaut du lien
}

