const SUPABASE_URL = 'https://irqqdwqhzrydsohpwzqo.supabase.co';
const ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlycXFkd3FoenJ5ZHNvaHB3enFvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjI5ODQ1NTQsImV4cCI6MjAzODU2MDU1NH0.-zYhW2AbwCKHCjS50nX-xJkiRd4wsZmqcTna9MkbjU8';
const TABLE_NAME = 'blogs'; 

const blogSection = document.getElementById('blogs'); 

async function getBlogPosts() {
    return await fetch(`${SUPABASE_URL}/rest/v1/${TABLE_NAME}?select=title,date,tags&order=date.desc`, {
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

function createNewBlogDOM(title, date, tags) {
    const blogSection = document.createElement('div');
    blogSection.className = 'blog-entry';

    const blogLink = document.createElement('a');
    blogLink.className = 'blog-link'; 
    blogLink.innerHTML = title;
    blogLink.href = '#'; 

    const blogInfo = document.createElement('p');
    blogInfo.innerHTML = (tags.length === 0) ? `${date}` : `${date}  • ${tags.join(', ')}`  

    blogSection.appendChild(blogLink);
    blogSection.appendChild(blogInfo);

    return blogSection;
}

addEventListener('DOMContentLoaded', async () => {
    const posts = await getBlogPosts(); 

    for(let i=0; i<posts.length; i++) { 
        blogSection.append(createNewBlogDOM(posts[i].title, posts[i].date, posts[i].tags));
    } 
});