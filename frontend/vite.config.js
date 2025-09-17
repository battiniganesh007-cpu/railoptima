import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Get the host from Replit environment
const host = process.env.REPL_SLUG
  ? `${process.env.REPL_SLUG}.${process.env.REPL_OWNER}.repl.co`
  : "localhost";

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    host: "0.0.0.0",
    allowedHosts: [
      host, // ✅ allow your replit.dev host dynamically
      ".replit.dev",
      ".repl.co"
    ]
  }
})
