const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("ReservationForm");
const submitButton = document.getElementById("submitButton");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("username_id");
    /**let commentId = e.target.getAttribute("name_id");**/
    let commentContent = document.getElementById(`comment${usernameId}`).innerText;
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    ReservationForm.setAttribute("action", `edit_comment/${usernameId}`);
  });
}