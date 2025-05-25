document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

    document.querySelector('#compose-form').onsubmit=function(){
        fetch('/emails', {
            method:'POST',
            body: JSON.stringify({
                recipients: document.querySelector('#compose-recipients').value,
                subject: document.querySelector('#compose-subject').value,
                body: document.querySelector('#compose-body').value
            })
        })
        .then(response => response.json())
        .then(result =>
            load_mailbox('inbox')
        );
    };

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

    if (mailbox === 'inbox'){
        fetch('/emails/inbox')
        .then(response => response.json())
        .then(emails => {
            const view = document.querySelector('#emails-view');

            emails.forEach(email => {
                const link = document.createElement('a');

                link.textContent = email.subject;
                link.style.cursor = 'pointer';
                link.style.color = 'blue';
                link.style.display = 'block';

                if (email.read) {
                    link.style.backgroundColor = 'lightgray';
                } else {
                    link.style.backgroundColor = 'white';
                }

                link.onclick = () => {
                    view.innerHTML = `
                        <p><strong>Sender:</strong> ${email.sender}</p>
                        <p><strong>Subject:</strong> ${email.subject}</p>
                        <p><strong>Time:</strong> ${email.timestamp}</p>
                        <hr>
                        <p>${email.body}</p>
                        <button id="archive-btn">
                            ${email.archived ? 'Un-archive' : 'Archive'}
                        </button>
                        <button id="reply">Reply</button>
                        `;

                    fetch(`/emails/${email.id}`, {
                        method: 'PUT',
                        body: JSON.stringify({ read: true })
                    })

                    document.querySelector('#archive-btn').addEventListener('click', () => {
                        fetch(`/emails/${email.id}`, {
                            method: 'PUT',
                            body: JSON.stringify({ archived: !email.archived })
                        })
                        .then(() => load_mailbox('inbox'));
                    });

                    document.querySelector('#reply').addEventListener('click', () => {


                      // Show compose view and hide other views
                      document.querySelector('#emails-view').style.display = 'none';
                      document.querySelector('#compose-view').style.display = 'block';

                      document.querySelector('#compose-recipients').value = email.sender;
                      document.querySelector('#compose-subject').value = 'Re: ' + email.subject;
                      document.querySelector('#compose-body').value = 'On ' + email.timestamp + ', ' + email.sender + ' wrote: '
                        + email.body;
                    
                    })
                };
                
                view.append(link);
                
            });
        })
    }
    if (mailbox === 'archive'){
        
        fetch('/emails/archive')
        .then(response => response.json())
        .then(emails => {
            const view = document.querySelector('#emails-view');

            emails.forEach(email => {
                const link = document.createElement('a');

                link.textContent = email.subject;
                link.style.cursor = 'pointer';
                link.style.color = 'blue';
                link.style.display = 'block';

                link.onclick = () => {
                    view.innerHTML = `
                        <p><strong>Sender:</strong> ${email.sender}</p>
                        <p><strong>Subject:</strong> ${email.subject}</p>
                        <p><strong>Time:</strong> ${email.timestamp}</p>
                        <hr>
                        <p>${email.body}</p>
                        <button id="archive-btn">
                            ${email.archived ? 'Un-archive' : 'Archive'}
                        </button>`;

                    document.querySelector('#archive-btn').addEventListener('click', () => {
                        fetch(`/emails/${email.id}`, {
                            method: 'PUT',
                            body: JSON.stringify({ archived: !email.archived })
                        })
                        .then(() => load_mailbox('inbox'));
                    });
                };
                
                view.append(link);
                
            });
        })
    }    


    if (mailbox === 'sent'){
        
        fetch('/emails/sent')
        .then(response => response.json())
        .then(emails => {
            const view = document.querySelector('#emails-view');

            emails.forEach(email => {
                const link = document.createElement('a');

                link.textContent = email.subject;
                link.style.cursor = 'pointer';
                link.style.color = 'blue';
                link.style.display = 'block';

                link.onclick = () => {
                    view.innerHTML = `
                        <p><strong>Sender:</strong> ${email.sender}</p>
                        <p><strong>Subject:</strong> ${email.subject}</p>
                        <p><strong>Time:</strong> ${email.timestamp}</p>
                        <hr>
                        <p>${email.body}</p>`
                };      
                view.append(link);
            });
        })
    }    
}
