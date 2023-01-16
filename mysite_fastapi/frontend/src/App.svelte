<script>
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"

  const routes = {
    '/': Home, // frontend/src/routes/Home.svelte
  }
</script>

<Router {routes}/>