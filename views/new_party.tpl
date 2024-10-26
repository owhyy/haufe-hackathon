%rebase ('head.tpl')

<main class="container" style="text-align: center;">
<article>
      <h1>Plan a new party</h1>
<form hx-post="/party" method="POST" style="display: flex; flex-direction: column; align-items: center; gap: 1rem; margin-top: 1.5rem;">
    <input type="text" name="partyName" placeholder="Name of the party" required />
    <input type="number" name="maxBudget" placeholder="Maximum budget" required />
    <input type="date" name="partyDate" required />
    <button type="submit">Create Party</button>
</form>
</article>
</main>