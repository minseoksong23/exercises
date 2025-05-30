const likeBtn = document.getElementById("like-button");
const likeCountSpan = document.getElementById("like-count");
const csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;

likeBtn.addEventListener("click", () => {

    const currentAction = likeBtn.textContent.trim().toLowerCase();
    const newAction = currentAction === "like" ? "like" : "unlike";

    const formData = new FormData();
    formData.append("action", newAction);

    const postId = likeBtn.getAttribute("data-post-id");
    fetch(`/like-post/${postId}/`, {
        method: "POST",
        body: formData,
        headers: { "X-CSRFToken": csrfToken },
        credentials: "same-origin"
    })
    .then(response => response.json())
    .then(data => {
        likeCountSpan.textContent = data.likes;

        if (newAction === "like"){
            likeBtn.textContent = "Unlike";
        } else {
            likeBtn.textContent = "Like";
        }
    })
    .catch(error => {
        console.error("Error in like toggle:", error);
    });
});
</script>
