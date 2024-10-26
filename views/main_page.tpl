% rebase('head.tpl')
<main class="container" style="text-align: center;">
    <h1>Party Planning</h1>
    <div class="grid" style="justify-content: center;">
        <button hx-get="/new-party" hx-target="body">Plan a new party!</button>
    </div>
    <div>
        <form hx-get="/get-party" hx-target="body" method="GET" style="margin-top: 2.5rem;">

            <fieldset role="group">
                <input maxlength="8" type="text" name="code" placeholder="Or join a party planning session" "/>
	      <button type="submit " >Join</button>
	      <!-- TODO: show error message here -->
	 </fieldset>
	 </form>
     </div>
</main>
