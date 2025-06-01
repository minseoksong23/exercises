document.addEventListener('DOMContentLoaded', () => {

    const csrftoken = document.querySelector('meta[name="csrf-token"]').content;

    document.querySelectorAll('.like-button').forEach(btn => {
        btn.addEventListener('click', () => {
            const postId = btn.dataset.postId;
            const action = btn.textContent.trim() === 'Like' ? 'like' : 'unlike';

            const formData = new FormData();
            formData.append('action', action);

            fetch(`/like-post/${postId}/`, {
                method: 'POST', 
                body: formData,
                headers: { 'X-CSRFToken': csrftoken },
                credentials: 'same-origin'
            })
            .then(r => r.json())
            .then(data => {
            document.getElementById(`like-count-${postId}`).textContent = data.likes;
            btn.textContent = btn.textContent.trim() === 'Like' ? 'Unlike' : 'Like';
            })
            .catch(err => console.error(err));
        })
    });
});
