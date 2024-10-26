%rebase ('head.tpl')

<main class="container" style="text-align: center;">
<article>
      <h1>Join planning session for {{party.name}}</h1>
<form hx-post="/party/{{party.code}}/join" method="POST" hx-target="body" style="display: flex; flex-direction: column; align-items: center; gap: 1rem; margin-top: 1.5rem;">
    <input type="text" name="username" placeholder="Choose a username" required />
    <button type="submit">Join session</button>
</form>
</article>
</main>