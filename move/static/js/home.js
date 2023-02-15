const sr = ScrollReveal({
  distance : '75px',
  duration : 2700,
  reset :true
})

sr.reveal('.about-text',{delay:350,origin:'left'});
sr.reveal('.about-img',{delay:350,origin:'right'});

sr.reveal('.homes-text',{delay:150,origin:'left'});
sr.reveal('.homes-img',{delay:150,origin:'right'});

sr.reveal('.containers,.about,.portfolio,.service,.cta,.contact',{delay:100,origin:'top'});