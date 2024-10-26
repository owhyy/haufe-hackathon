%rebase ('head.tpl')

<main class="container" style="text-align: center;">
<article>
      <h1>Add a new thing</h1>
<form hx-post="/party/{{party.id}}/thing" method="POST" style="display: flex; flex-direction: column; align-items: center; gap: 1rem; margin-top: 1.5rem;">
    <input type="text" name="name" placeholder="Name of thing" required />
    <input type="text" name="description" placeholder="Description of thing" required />    
    <input type="number" name="price" placeholder="Price" required />
    <button type="submit">Create thing</button>
</form>
</article>
</main>