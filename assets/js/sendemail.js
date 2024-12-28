function sendMail(contactForm) {
    emailjs.send("service_mfj2q7y", "Roshan", {
            "from_name": contactForm.name.value,
            "from_email": contactForm.emailaddress.value,
            "ideas and feedback": contactForm.feedbacksummary.value
        })
        .then(
            function (response) {
                console.log("SUCCESS", response);
            },
            function (error) {
                console.log("FAILED", error);
            }
        );
}
