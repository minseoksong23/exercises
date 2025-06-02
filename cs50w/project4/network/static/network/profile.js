document.addEventListener('DOMContentLoaded', () => {

    const csrftoken = document.querySelector('meta[name="csrf-token"]').content;
    btn = document.querySelector('.follow-button')
    btn.addEventListener('click', () => {
        const user_id = btn.dataset.userId;
        const action = btn.textContent === 'follow' ? 'follow' : 'unfollow';

        const formData = new FormData();
        formData.append('action', action);

        fetch(`/profile/${user_id}/`, {
            method: 'POST', 
            body: formData,
            headers: { 'X-CSRFToken': csrftoken },
            credentials: 'same-origin'
        })
        .then(r => r.json())
        .then(data => {
        document.getElementById(`follower-${user_id}`).textContent = data.follower_ct;
        document.getElementById(`following-${user_id}`).textContent = data.following_ct;
        btn.textContent = btn.textContent.trim() === 'follow' ? 'unfollow' : 'follow';
        })
        .catch(err => console.error(err));
    })
});

