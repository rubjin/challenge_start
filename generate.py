import os

BASE_DIR = "c:/Users/SO26074/Documents/챌린지_start/src"

FILES = {
    "html/challenge.html": """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>챌린지 목록 - 퍼블리싱</title>
  <link rel="stylesheet" href="../css/main.css">
</head>
<body>
  <div class="ch-challenge-layout">
    <header class="ch-challenge-header">
      <h1>챌린지</h1>
    </header>
    
    <nav class="ch-tab">
      <button type="button" class="ch-tab__item is-active">진행중인 챌린지</button>
      <button type="button" class="ch-tab__item">종료된 챌린지</button>
    </nav>

    <div class="ch-challenge-list">
      <!-- Challenge Card 1 -->
      <article class="ch-card">
        <img src="https://via.placeholder.com/300x160" alt="챌린지 썸네일" class="ch-card__thumb" />
        <div class="ch-card__content">
          <span class="ch-badge ch-badge--ongoing">진행중</span>
          <h2 class="ch-card__title">매일 아침 6시 기상하기</h2>
          <p class="ch-card__desc">건강한 습관을 만들어보세요.</p>
          <button type="button" class="ch-btn ch-btn--primary">참여하기</button>
        </div>
      </article>

      <!-- Challenge Card 2 -->
      <article class="ch-card">
        <img src="https://via.placeholder.com/300x160" alt="챌린지 썸네일" class="ch-card__thumb" />
        <div class="ch-card__content">
          <span class="ch-badge ch-badge--completed">종료</span>
          <h2 class="ch-card__title">주 3회 런닝하기</h2>
          <p class="ch-card__desc">체력을 기르는 러닝 챌린지</p>
          <button type="button" class="ch-btn ch-btn--outline is-disabled" disabled>기록보기</button>
        </div>
      </article>
    </div>
  </div>
</body>
</html>
""",
    "scss/main.scss": """@import 'base/reset';
@import 'base/variables';
@import 'base/mixins';
@import 'base/common';

@import 'components/button';
@import 'components/badge';
@import 'components/tab';
@import 'components/card';

@import 'pages/challenge';
""",
    "scss/base/_reset.scss": """* { margin: 0; padding: 0; box-sizing: border-box; }
ul, ol, li { list-style: none; }
a { text-decoration: none; color: inherit; }
button { border: none; background: none; cursor: pointer; }
""",
    "scss/base/_variables.scss": """$ch-primary: #3b82f6;
$ch-primary-hover: #2563eb;
$ch-gray-100: #f3f4f6;
$ch-gray-300: #d1d5db;
$ch-gray-800: #1f2937;
$ch-white: #ffffff;
$ch-radius-md: 8px;
$ch-radius-lg: 12px;
""",
    "scss/base/_mixins.scss": """@mixin flex-center {
  display: flex;
  align-items: center;
  justify-content: center;
}
@mixin text-ellipsis {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
""",
    "scss/base/_common.scss": """body { font-family: 'Pretendard', sans-serif; color: $ch-gray-800; line-height: 1.5; }
.ch-a11y-hidden { position: absolute; width: 1px; height: 1px; margin: -1px; overflow: hidden; clip: rect(0, 0, 0, 0); }
""",
    "scss/components/_button.scss": """.ch-btn {
  display: inline-flex; align-items: center; justify-content: center;
  padding: 10px 20px; border-radius: $ch-radius-md; font-weight: 600;
  transition: background-color 0.2s;
  &--primary {
    background-color: $ch-primary; color: $ch-white;
    &:hover { background-color: $ch-primary-hover; }
  }
  &--outline {
    border: 1px solid $ch-gray-300; background-color: $ch-white; color: $ch-gray-800;
    &:hover { background-color: $ch-gray-100; }
  }
  &:disabled, &.is-disabled {
    opacity: 0.5; cursor: not-allowed; pointer-events: none;
  }
}
""",
    "scss/components/_badge.scss": """.ch-badge {
  display: inline-block; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold;
  &--ongoing { background-color: rgba($ch-primary, 0.1); color: $ch-primary; }
  &--completed { background-color: $ch-gray-100; color: $ch-gray-800; }
}
""",
    "scss/components/_tab.scss": """.ch-tab {
  display: flex; border-bottom: 1px solid $ch-gray-300;
  &__item {
    padding: 12px 24px; font-weight: 600; color: $ch-gray-300; position: relative;
    &.is-active {
      color: $ch-gray-800;
      &::after { content: ''; position: absolute; bottom: -1px; left: 0; right: 0; height: 2px; background-color: $ch-gray-800; }
    }
  }
}
""",
    "scss/components/_card.scss": """.ch-card {
  border: 1px solid $ch-gray-300; border-radius: $ch-radius-lg; overflow: hidden; background-color: $ch-white;
  &__thumb {
    width: 100%; height: 160px; background-color: $ch-gray-100; object-fit: cover;
  }
  &__content { padding: 16px; }
  &__title { font-size: 18px; font-weight: bold; margin-bottom: 8px; @include text-ellipsis; }
  &__desc { font-size: 14px; color: $ch-gray-800; margin-bottom: 16px; }
}
""",
    "scss/pages/_challenge.scss": """.ch-challenge-layout {
  max-width: 1200px; margin: 0 auto; padding: 40px 20px;
}
.ch-challenge-header {
  margin-bottom: 32px;
  h1 { font-size: 28px; font-weight: bold; }
}
.ch-challenge-list {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 24px; margin-top: 24px;
}
""",
    "css/main.css": """* { margin: 0; padding: 0; box-sizing: border-box; }
ul, ol, li { list-style: none; }
a { text-decoration: none; color: inherit; }
button { border: none; background: none; cursor: pointer; }
body { font-family: 'Pretendard', sans-serif; color: #1f2937; line-height: 1.5; }
.ch-a11y-hidden { position: absolute; width: 1px; height: 1px; margin: -1px; overflow: hidden; clip: rect(0, 0, 0, 0); }
.ch-btn { display: inline-flex; align-items: center; justify-content: center; padding: 10px 20px; border-radius: 8px; font-weight: 600; transition: background-color 0.2s; }
.ch-btn--primary { background-color: #3b82f6; color: #ffffff; }
.ch-btn--primary:hover { background-color: #2563eb; }
.ch-btn--outline { border: 1px solid #d1d5db; background-color: #ffffff; color: #1f2937; }
.ch-btn--outline:hover { background-color: #f3f4f6; }
.ch-btn:disabled, .ch-btn.is-disabled { opacity: 0.5; cursor: not-allowed; pointer-events: none; }
.ch-badge { display: inline-block; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold; }
.ch-badge--ongoing { background-color: rgba(59, 130, 246, 0.1); color: #3b82f6; }
.ch-badge--completed { background-color: #f3f4f6; color: #1f2937; }
.ch-tab { display: flex; border-bottom: 1px solid #d1d5db; }
.ch-tab__item { padding: 12px 24px; font-weight: 600; color: #d1d5db; position: relative; }
.ch-tab__item.is-active { color: #1f2937; }
.ch-tab__item.is-active::after { content: ''; position: absolute; bottom: -1px; left: 0; right: 0; height: 2px; background-color: #1f2937; }
.ch-card { border: 1px solid #d1d5db; border-radius: 12px; overflow: hidden; background-color: #ffffff; }
.ch-card__thumb { width: 100%; height: 160px; background-color: #f3f4f6; object-fit: cover; }
.ch-card__content { padding: 16px; }
.ch-card__title { font-size: 18px; font-weight: bold; margin-bottom: 8px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.ch-card__desc { font-size: 14px; color: #1f2937; margin-bottom: 16px; }
.ch-challenge-layout { max-width: 1200px; margin: 0 auto; padding: 40px 20px; }
.ch-challenge-header { margin-bottom: 32px; }
.ch-challenge-header h1 { font-size: 28px; font-weight: bold; }
.ch-challenge-list { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 24px; margin-top: 24px; }
"""
}

for path, content in FILES.items():
    full_path = os.path.join(BASE_DIR, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Scaffolding complete.")
