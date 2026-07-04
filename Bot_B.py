<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Una Galaxia de Amor para Ti</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: "Helvetica Neue", Arial, sans-serif;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      background: #020005;
      color: white;
      overflow: hidden;
      height: 100vh;
      width: 100vw;
      position: relative;
    }

    /* กาแล็กซี่ 3 มิติ */
    #universe {
      position: absolute;
      top: 50%;
      left: 50%;
      width: 100vw;
      height: 100vh;
      transform: translate(-50%, -50%);
      perspective: 800px;
      z-index: 1;
    }

    #galaxy-plane {
      position: absolute;
      top: 50%;
      left: 50%;
      width: 800px;
      height: 800px;
      transform-style: preserve-3d;
      transform: translate(-50%, -50%) rotateX(72deg);
    }

    .galaxy-spin {
      position: absolute;
      width: 100%;
      height: 100%;
      animation: spinGalaxy 25s linear infinite;
    }

    @keyframes spinGalaxy {
      from { transform: rotateZ(0deg); }
      to { transform: rotateZ(360deg); }
    }

    /* ละอองดาวของกาแล็กซี่ */
    #galaxy-particles {
      width: 2px;
      height: 2px;
      border-radius: 50%;
      position: absolute;
      top: 50%;
      left: 50%;
    }

    /* หลุมดำตรงกลาง */
    .black-hole {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 60px;
      height: 60px;
      background: #000;
      border-radius: 50%;
      box-shadow: 
        0 0 30px 15px rgba(255, 20, 147, 0.9),
        0 0 60px 30px rgba(255, 0, 100, 0.4),
        inset 0 0 15px 5px #000;
      z-index: 5;
    }

    /* ข้อความที่โคจรรอบกาแล็กซี่ */
    .word {
      position: absolute;
      top: 50%;
      left: 50%;
      color: #ff9bd1;
      font-weight: bold;
      font-size: 14px;
      letter-spacing: 1px;
      text-shadow: 0 0 10px #ff1493, 0 0 20px #ff1493;
      white-space: nowrap;
    }

    /* ตัวการ์ตูนลอยๆ */
    .floating-emoji {
      position: absolute;
      font-size: 30px;
      filter: drop-shadow(0 0 10px rgba(255,100,150,0.8));
      z-index: 10;
      animation: floatItem 3s ease-in-out infinite alternate;
    }
    
    @keyframes floatItem {
      from { transform: translateY(0) rotate(-10deg); }
      to { transform: translateY(-15px) rotate(10deg); }
    }

    /* หัวใจที่ลอยอยู่เหนือหลุมดำ */
    #heart-container {
      position: absolute;
      top: 45%;
      left: 50%;
      transform: translate(-50%, -160px);
      z-index: 6;
      animation: heartPulse 2s ease-in-out infinite;
    }

    #heart-particles {
      width: 2px;
      height: 2px;
      border-radius: 50%;
      position: absolute;
      top: 0;
      left: 0;
    }

    @keyframes heartPulse {
      0%, 100% { transform: translate(-50%, -160px) scale(1); }
      50% { transform: translate(-50%, -160px) scale(1.08); }
    }

    /* หน้าต่างโค้ดมุมซ้ายล่าง */
    .code-window {
      position: absolute;
      bottom: 85px;
      left: 15px;
      width: 260px;
      background: #0d1421;
      border-radius: 12px;
      padding: 15px;
      font-family: monospace;
      font-size: 11px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.6);
      z-index: 40;
      border: 1px solid rgba(255,255,255,0.05);
    }
    .code-header {
      text-align: right;
      color: #7a8496;
      margin-bottom: 12px;
      font-size: 9px;
    }
    .code-line { line-height: 1.6; }
    .c-num { color: #4e5a6e; margin-right: 12px; display: inline-block; width: 10px; }
    .c-sel { color: #ffcb6b; }
    .c-prop { color: #82aaff; }
    .c-val { color: #f78c6c; }
    .c-str { color: #c3e88d; }
    .c-func { color: #c792ea; }
    .c-var { color: #ff5370; }

    /* TikTok UI Overlay */
    .tiktok-ui {
      position: absolute;
      right: 15px;
      bottom: 100px;
      display: flex;
      flex-direction: column;
      gap: 18px;
      z-index: 50;
    }
    .tk-icon {
      display: flex;
      flex-direction: column;
      align-items: center;
      font-size: 11px;
      font-weight: 600;
      text-shadow: 0 1px 3px rgba(0,0,0,0.8);
    }
    .tk-circle {
      width: 36px;
      height: 36px;
      background: rgba(0,0,0,0.2);
      border-radius: 50%;
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: 20px;
      margin-bottom: 4px;
    }

    .tk-caption {
      position: absolute;
      bottom: 15px;
      left: 15px;
      right: 60px;
      z-index: 50;
      text-shadow: 0 1px 3px rgba(0,0,0,0.8);
    }
    .tk-user { font-weight: bold; font-size: 15px; margin-bottom: 5px; }
    .tk-desc { font-size: 13px; line-height: 1.3; margin-bottom: 5px; color: #eee; }
    .tk-music { font-size: 12px; }

    /* การ์ดข้อความ (Para Siempre) */
    .message-card {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 290px;
      background: linear-gradient(to bottom, #2b1115, #140508);
      border-radius: 20px;
      padding: 20px;
      text-align: center;
      z-index: 100;
      box-shadow: 0 0 50px rgba(255, 20, 100, 0.3), inset 0 0 20px rgba(255,255,255,0.03);
      border: 1px solid rgba(255, 100, 150, 0.1);
    }

    .card-art {
      width: 100%;
      height: 170px;
      background: #3e1b1a;
      border-radius: 12px;
      margin-bottom: 20px;
      overflow: hidden;
    }

    .message-card h2 {
      font-family: "Georgia", serif;
      font-size: 20px;
      margin-bottom: 10px;
      color: #fff;
    }

    .message-card p {
      font-size: 10.5px;
      line-height: 1.6;
      color: #ccc;
      margin-bottom: 25px;
      padding: 0 10px;
    }

    .message-card button {
      background: transparent;
      border: 1px solid #ff4fa3;
      color: #ff4fa3;
      padding: 8px 25px;
      border-radius: 20px;
      font-size: 10px;
      font-weight: bold;
      letter-spacing: 1px;
      cursor: pointer;
    }

    .heart-badge {
      position: absolute;
      bottom: -15px;
      right: 20px;
      background: white;
      width: 30px;
      height: 30px;
      border-radius: 50%;
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: 16px;
      box-shadow: 0 5px 15px rgba(0,0,0,0.5);
    }
  </style>
</head>
<body>

  <div id="universe">
    <div id="galaxy-plane">
      <div class="galaxy-spin">
        <div id="galaxy-particles"></div>
        <div class="black-hole"></div>

        <div class="word" style="transform: translate(-50%, -50%) rotate(0deg) translateY(220px) rotate(-90deg)">MI AMOR ETERNO ∞</div>
        <div class="word" style="transform: translate(-50%, -50%) rotate(45deg) translateY(280px) rotate(-90deg)">HAPPY BIRTHDAY</div>
        <div class="word" style="transform: translate(-50%, -50%) rotate(100deg) translateY(310px) rotate(-90deg)">TE ADORO</div>
        <div class="word" style="transform: translate(-50%, -50%) rotate(140deg) translateY(240px) rotate(-90deg)">ERES MAGIA ∞</div>
        <div class="word" style="transform: translate(-50%, -50%) rotate(200deg) translateY(290px) rotate(-90deg)">LOCURA</div>
        <div class="word" style="transform: translate(-50%, -50%) rotate(250deg) translateY(210px) rotate(-90deg)">SIEMPRE JUNTOS</div>
        <div class="word" style="transform: translate(-50%, -50%) rotate(310deg) translateY(330px) rotate(-90deg)">NUESTRO UNIVERSO</div>
      </div>
    </div>
  </div>

  <div id="heart-container">
    <div id="heart-particles"></div>
  </div>

  <div class="floating-emoji" style="top: 25%; right: 20%;">🐱🎀</div>
  <div class="floating-emoji" style="top: 35%; right: 10%;">🕷️❤️</div>
  <div class="floating-emoji" style="bottom: 40%; left: 15%;">🐶</div>

  <div class="message-card" id="msg-card">
    <div class="card-art">
      <svg width="100%" height="100%" viewBox="0 0 200 170" xmlns="http://www.w3.org/2000/svg">
        <rect width="200" height="170" fill="#2d1314"/>
        <circle cx="100" cy="85" r="60" fill="#a45535" opacity="0.5" filter="blur(5px)"/>
        <path d="M 60 170 Q 75 100 85 85 Q 90 70 80 60 Q 65 50 65 70 Q 65 120 40 170" fill="#eed9b6"/>
        <circle cx="75" cy="50" r="14" fill="#eed9b6"/>
        <path d="M 140 170 Q 125 100 115 85 Q 110 70 120 60 Q 135 50 135 70 Q 135 120 160 170" fill="#dcb180"/>
        <circle cx="125" cy="50" r="14" fill="#dcb180"/>
        <path d="M 75 110 L 80 105 L 85 110 L 80 120 Z" fill="#111"/>
        <path d="M 125 110 L 120 105 L 115 110 L 120 120 Z" fill="#111"/>
        <path d="M 85 110 Q 100 100 115 110" stroke="#fff" stroke-width="1.5" stroke-dasharray="3,3" fill="none" opacity="0.6"/>
      </svg>
    </div>
    <h2>Para Siempre</h2>
    <p>No me importa cuántas vidas tenga que vivir, en<br>cada una de ellas te elegiré a ti. Para siempre y un<br>día más.</p>
    <button onclick="document.getElementById('msg-card').style.display='none'">VOLVER ❤️</button>
    <div class="heart-badge">💬</div>
  </div>

  <div class="code-window">
    <div class="code-header">Style.css</div>
    <div class="code-line"><span class="c-num">1</span><span class="c-sel">.Para_Ti</span> {</div>
    <div class="code-line"><span class="c-num">2</span>&nbsp;&nbsp;<span class="c-prop">position</span>: <span class="c-val">absolute</span>;</div>
    <div class="code-line"><span class="c-num">3</span>&nbsp;&nbsp;<span class="c-prop">width</span>: <span class="c-val">90%</span>;</div>
    <div class="code-line"><span class="c-num">4</span>&nbsp;&nbsp;<span class="c-prop">font-size</span>: <span class="c-val">2rem</span>;</div>
    <div class="code-line"><span class="c-num">5</span>&nbsp;&nbsp;<span class="c-prop">font-family</span>: <span class="c-str">"Te Amo"</span>;</div>
    <div class="code-line"><span class="c-num">6</span>&nbsp;&nbsp;<span class="c-prop">height</span>: <span class="c-func">var</span>(<span class="c-var">--letter-love</span>);</div>
    <div class="code-line"><span class="c-num">7</span>&nbsp;&nbsp;<span class="c-prop">transform</span>: <span class="c-func">translateX</span>(<span class="c-val">-50%</span>);</div>
    <div class="code-line"><span class="c-num">8</span>&nbsp;&nbsp;<span class="c-prop">background</span>: <span class="c-func">var</span>(<span class="c-var">--letter</span>);</div>
    <div class="code-line"><span class="c-num">9</span>}</div>
  </div>

  <div class="tiktok-ui">
    <div class="tk-icon">
      <div class="tk-circle" style="color: #ff2a5f;">❤️</div>
      <span>50.7K</span>
    </div>
    <div class="tk-icon">
      <div class="tk-circle">💬</div>
      <span>344</span>
    </div>
    <div class="tk-icon">
      <div class="tk-circle">🔖</div>
      <span>23.3K</span>
    </div>
    <div class="tk-icon">
      <div class="tk-circle">↪️</div>
      <span>3,226</span>
    </div>
  </div>

  <div class="tk-caption">
    <div class="tk-user">AlexDev | Web Developer</div>
    <div class="tk-desc">Happy Birthday My Love Galaxia de cumpleaños para dedicar a es... <span style="font-weight:bold">เพิ่มเติม</span></div>
    <div class="tk-music">🎵 Sign of the Times - @Har...</div>
  </div>

  <script>
    // สคริปต์สำหรับสร้าง Particle Effect ด้วย Box-shadow (ทำให้ได้ภาพละอองดาว 3 มิติ)
    window.onload = () => {
      // 1. สร้างละอองดาวให้กาแล็กซี่
      const galaxy = document.getElementById('galaxy-particles');
      let shadows = [];
      const numStars = 1500;
      
      for(let i = 0; i < numStars; i++) {
        let arm = i % 3; // สร้างแขนเกลียว 3 แขน
        let radius = Math.random() * 400; // รัศมีวงกว้างสุด
        // คำนวณสมการก้นหอย (Spiral Equation)
        let angle = (radius * 0.02) + (arm * (Math.PI * 2 / 3));
        
        // กระจายตัวออกจากเส้นแขนหลักเล็กน้อย
        let spread = radius * 0.15;
        let x = radius * Math.cos(angle) + (Math.random() - 0.5) * spread;
        let y = radius * Math.sin(angle) + (Math.random() - 0.5) * spread;

        // ไล่เฉดสีจากสว่างตรงกลางไปสีชมพูเข้มขอบนอก
        let color = '';
        let opacity = Math.random() * 0.8 + 0.2;
        if(radius < 60) color = `rgba(255, 255, 255, ${opacity})`;
        else if (radius < 180) color = `rgba(255, 120, 200, ${opacity})`;
        else color = `rgba(255, 0, 130, ${opacity})`;

        let size = Math.random() > 0.85 ? '2px' : '1px';
        shadows.push(`${x}px ${y}px 0 ${size} ${color}`);
      }
      galaxy.style.boxShadow = shadows.join(',');

      // 2. สร้างละอองดาวให้รูปหัวใจ 3 มิติ
      const heart = document.getElementById('heart-particles');
      let heartShadows = [];
      const numHeartParticles = 1200;

      for(let i = 0; i < numHeartParticles; i++) {
        let t = Math.random() * Math.PI * 2;
        let scale = 5.5 + Math.random() * 3.5; // ความหนาของละอองหัวใจ
        
        // สมการคณิตศาสตร์สร้างรูปหัวใจ (Parametric Heart Equation)
        let x = 16 * Math.pow(Math.sin(t), 3) * scale;
        let y = -(13 * Math.cos(t) - 5 * Math.cos(2*t) - 2 * Math.cos(3*t) - Math.cos(4*t)) * scale;

        // ให้ฟุ้งกระจายเล็กน้อย
        x += (Math.random() - 0.5) * 15;
        y += (Math.random() - 0.5) * 15;

        let op = Math.random() * 0.8 + 0.2;
        let color = `rgba(255, ${Math.floor(Math.random() * 50 + 50)}, ${Math.floor(Math.random() * 100 + 150)}, ${op})`;
        let size = Math.random() > 0.8 ? '3px' : '1px';
        heartShadows.push(`${x}px ${y}px 0 ${size} ${color}`);
      }
      heart.style.boxShadow = heartShadows.join(',');
    };
  </script>
</body>
</html> 
