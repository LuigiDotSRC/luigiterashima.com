const SUPABASE_URL = 'https://irqqdwqhzrydsohpwzqo.supabase.co';
const ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlycXFkd3FoenJ5ZHNvaHB3enFvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjI5ODQ1NTQsImV4cCI6MjAzODU2MDU1NH0.-zYhW2AbwCKHCjS50nX-xJkiRd4wsZmqcTna9MkbjU8';
const TABLE_NAME = 'blogs'; 

const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const id = urlParams.get('id');

async function fetchPost() {
    return await fetch(`${SUPABASE_URL}/rest/v1/${TABLE_NAME}?id=eq.${id}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'apikey': ANON_KEY, 
            'Authorization': `Bearer ${ANON_KEY}`
        }
    })
    .then(response => {
        if (response.status == 200) {
            return response.json(); 
        } else {
            throw new Error(response.status); 
        }
    });
}

addEventListener('DOMContentLoaded', async () => {
    const post = await fetchPost();

    const titleElement = document.querySelector('title');
    titleElement.textContent = `~/blog/${post[0].title}`;

    const data = document.getElementById('data');
    data.innerText = `${post[0].date} \nabout: ${post[0].tags.join(', ')}`;

    const title = document.getElementById('title');
    title.innerHTML = `/blog/${post[0].title}`; 

    const readarea = document.getElementById('readarea');
    readarea.innerHTML = post[0].content; 
});