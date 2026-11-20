import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
// India dashboard runs on 5174 so it can run next to the US one (5173).
export default defineConfig({
  plugins: [react()],
  server: { port: 5174, strictPort: true },
})
