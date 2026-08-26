import { defineConfig } from 'vite';
import { resolve } from 'path';
import fs from 'fs';

// 초간단 HTML Include 플러그인 (정규식 기반)
function htmlIncludePlugin() {
  return {
    name: 'html-include',
    transformIndexHtml(html) {
      // 주석(<!-- ... -->) 안에 있는 include는 무시하고, 실제 <include> 태그만 파일 내용으로 치환합니다.
      return html.replace(/<!--[\s\S]*?-->|<include\s+src="([^"]+)"><\/include>/g, (match, src) => {
        // 매칭된 내용이 주석이라면 원본 그대로 통과
        if (match.startsWith('<!--')) return match;
        
        // vite.config.js 파일의 위치(__dirname) 기준으로 경로 탐색
        const filePath = resolve(__dirname, src);
        if (fs.existsSync(filePath)) {
          return fs.readFileSync(filePath, 'utf-8');
        }
        console.warn(`[html-include] 파일을 찾을 수 없습니다: ${filePath}`);
        return match; // 파일이 없으면 원본 그대로 둠
      });
    },
    handleHotUpdate({ file, server }) {
      if (file.endsWith('.html')) {
        server.ws.send({
          type: 'full-reload'
        });
      }
    }
  };
}

export default defineConfig({
  plugins: [htmlIncludePlugin()],
  server: {
    port: 3000,
    open: true // 서버 실행 시 브라우저 자동 열기
  }
});
