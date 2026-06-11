import pygame
import sys
import math
import random
import json
import os
import time
from datetime import datetime

# ── Dil sistemi ───────────────────────────────────────────────────────────────
LANG = {'current': 'tr'}

TRANSLATIONS = {
    'tr': {
        'menu_start':        'Oyuna Başlat',
        'menu_highscores':   'Yüksek Skorlar',
        'menu_howtoplay':    'Nasıl Oynanır',
        'menu_settings':     'Ayarlar',
        'menu_exit':         'Çıkış',
        'menu_subtitle':     'Tuğlaları Kır, Rekoru Geç!',
        'menu_hint':         '↑ ↓  Seçim     ENTER  Onayla     ESC  Çıkış',
        'hud_score':         'Skor',
        'hud_lives':         'Can',
        'hud_level':         'Bölüm',
        'badge_big_paddle':  'Raket+',
        'badge_small_paddle':'Raket-',
        'badge_ghost':       'Hayalet',
        'badge_speed':       'Hızlı',
        'badge_small_ball':  'Top-',
        'badge_big_ball':    'Top+',
        'badge_sticky':      'Yapışkan',
        'badge_fire':        'Ateş',
        'badge_barrier':     'Bariyer',
        'ready':             'Hazır mısın?',
        'launch_hint':       'Space / Mouse Tıkla - Topu Fırlat',
        'launch_hint2':      'Space / Tıkla — Topu Fırlat',
        'fire_hint':         'Tıkla / Space — Ateş Et!',
        'paused':            'Duraklatıldı',
        'pause_hint':        'Devam etmek için Space tuşuna basın',
        'completed':         'Oyunu Tamamladınız!',
        'total_score':       'Toplam Puan',
        'game_over_text':    'Oyun Bitti!',
        'score_label':       'Puan',
        'level_label':       'Bölüm',
        'blocks_destroyed':  'Kırılan Blok',
        'powers_collected':  'Toplanan Güç',
        'rank_label':        'Sıralamanız',
        'rank_suffix':       '. sırada!',
        'rank_outside':      'İlk 10 dışında',
        'restart_hint':      'Tekrar oynamak için R tuşuna basın',
        'menu_esc':          'Menü için Esc tuşuna basın',
        'new_record':        'Yeni Rekor!',
        'your_score':        'Puanınız',
        'enter_name':        'Adınızı Girin:',
        'save_hint':         'Kaydetmek için Enter tuşuna basın',
        'hs_empty':          'Henüz skor yok',
        'hs_col_name':       'İsim',
        'hs_col_score':      'Puan',
        'hs_col_level':      'Bölüm',
        'hs_col_date':       'Tarih',
        'back_esc':          'Menüye dönmek için ESC',
        'settings_title':    'Ayarlar',
        'sfx_label':         'Ses Efektleri',
        'music_label':       'Müzik',
        'fps_label':         'FPS',
        'lang_label':        'Dil',
        'lang_value':        'Türkçe',
        'settings_hint':     '← → : Değer  |  ↑ ↓ : Seçim  |  ESC / ENTER : Kaydet & Geri',
        'htp_title':         'Nasıl Oynanır?',
        'htp_back':          'Menüye dönmek için ESC',
        'htp_sec_controls':  'Kontroller:',
        'htp_sec_powers':    'Güçlendirmeler (30 saniye):',
        'htp_sec_blocks':    'Özel Bloklar:',
        'htp_sec_levels':    'Zorluk Seviyeleri:',
    },
    'en': {
        'menu_start':        'Start Game',
        'menu_highscores':   'High Scores',
        'menu_howtoplay':    'How to Play',
        'menu_settings':     'Settings',
        'menu_exit':         'Exit',
        'menu_subtitle':     'Break Bricks, Beat the Record!',
        'menu_hint':         '↑ ↓  Select     ENTER  Confirm     ESC  Exit',
        'hud_score':         'Score',
        'hud_lives':         'Lives',
        'hud_level':         'Level',
        'badge_big_paddle':  'Paddle+',
        'badge_small_paddle':'Paddle-',
        'badge_ghost':       'Ghost',
        'badge_speed':       'Fast',
        'badge_small_ball':  'Ball-',
        'badge_big_ball':    'Ball+',
        'badge_sticky':      'Sticky',
        'badge_fire':        'Fire',
        'badge_barrier':     'Barrier',
        'ready':             'Ready?',
        'launch_hint':       'Space / Mouse Click - Launch Ball',
        'launch_hint2':      'Space / Click — Launch Ball',
        'fire_hint':         'Click / Space — Fire!',
        'paused':            'Paused',
        'pause_hint':        'Press Space to continue',
        'completed':         'You Completed the Game!',
        'total_score':       'Total Score',
        'game_over_text':    'Game Over!',
        'score_label':       'Score',
        'level_label':       'Level',
        'blocks_destroyed':  'Blocks Destroyed',
        'powers_collected':  'Powers Collected',
        'rank_label':        'Your Rank',
        'rank_suffix':       '. place!',
        'rank_outside':      'Outside Top 10',
        'restart_hint':      'Press R to play again',
        'menu_esc':          'Press Esc for Menu',
        'new_record':        'New Record!',
        'your_score':        'Your Score',
        'enter_name':        'Enter Your Name:',
        'save_hint':         'Press Enter to save',
        'hs_empty':          'No scores yet',
        'hs_col_name':       'Name',
        'hs_col_score':      'Score',
        'hs_col_level':      'Level',
        'hs_col_date':       'Date',
        'back_esc':          'Press ESC to return to menu',
        'settings_title':    'Settings',
        'sfx_label':         'Sound Effects',
        'music_label':       'Music',
        'fps_label':         'FPS',
        'lang_label':        'Language',
        'lang_value':        'English',
        'settings_hint':     '← → : Value  |  ↑ ↓ : Select  |  ESC / ENTER : Save & Back',
        'htp_title':         'How to Play?',
        'htp_back':          'Press ESC to return to menu',
        'htp_sec_controls':  'Controls:',
        'htp_sec_powers':    'Power-ups (30 seconds):',
        'htp_sec_blocks':    'Special Blocks:',
        'htp_sec_levels':    'Difficulty Levels:',
    }
}

def T(key):
    return TRANSLATIONS[LANG['current']].get(key, key)

# pip install nuitka
# pip install pygame

# Pygame'i başlat
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

# Tam ekran için ekran bilgilerini al
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

FPS = 60

# Çerçeve ayarları
FRAME_THICKNESS = 8

# Oyun alanı
GAME_AREA_X = FRAME_THICKNESS
GAME_AREA_Y = FRAME_THICKNESS
GAME_AREA_WIDTH = SCREEN_WIDTH - (FRAME_THICKNESS * 2)
GAME_AREA_HEIGHT = SCREEN_HEIGHT

# Renkler
COLORS = {
    'BLACK': (0, 0, 0),
    'WHITE': (255, 255, 255),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255),
    'YELLOW': (255, 255, 0),
    'PURPLE': (128, 0, 128),
    'ORANGE': (255, 165, 0),
    'CYAN': (0, 255, 255),
    'PINK': (255, 192, 203),
    'DARK_BLUE': (25, 25, 112),
    'DARK_GREEN': (0, 100, 0),
    'DARK_RED': (139, 0, 0),
    'GOLD': (255, 215, 0),
    'SILVER': (192, 192, 192),
    'BRONZE': (205, 127, 50),
    'GRAY': (128, 128, 128),
    'DARK_GRAY': (64, 64, 64),
    'LIME': (50, 205, 50),
    'HOT_PINK': (255, 105, 180),
    'DARK_ORANGE': (255, 140, 0),
    'INDESTRUCTIBLE': (30, 30, 30),
    'MENU_BG': (20, 20, 40),
    'BARRIER': (100, 80, 60),
    'WALL': (40, 40, 60),
    'PADDLE_GRADIENT_TOP': (150, 150, 200),
    'PADDLE_GRADIENT_BOTTOM': (80, 80, 130)
}

# Her level için farklı arka plan renkleri
LEVEL_BACKGROUNDS = {
    1: (10, 10, 30),
    2: (30, 10, 30),
    3: (10, 30, 20),
    4: (20, 20, 50),
    5: (30, 20, 40),
    6: (40, 20, 30),
    7: (30, 30, 40),
    8: (20, 20, 45),
    9: (25, 25, 50),
    10: (15, 15, 55)
}

# Paddle özellikleri
PADDLE_WIDTH = int(GAME_AREA_WIDTH * 0.08)
PADDLE_HEIGHT = int(GAME_AREA_HEIGHT * 0.025)
PADDLE_SPEED = int(GAME_AREA_WIDTH * 0.01)
PADDLE_MIN_WIDTH = int(GAME_AREA_WIDTH * 0.05)
PADDLE_MAX_WIDTH = int(GAME_AREA_WIDTH * 0.20)

# Top özellikleri
BALL_RADIUS = int(GAME_AREA_WIDTH * 0.006)
BALL_MIN_RADIUS = int(GAME_AREA_WIDTH * 0.004)
BALL_MAX_RADIUS = int(GAME_AREA_WIDTH * 0.012)  # Büyük top %10 daha küçültüldü (0.014'ten 0.012'ye)
BALL_SPEED_X = int(GAME_AREA_WIDTH * 0.006)
BALL_SPEED_Y = -int(GAME_AREA_HEIGHT * 0.007)
MAX_BALL_SPEED = int(GAME_AREA_WIDTH * 0.022)

# Blok özellikleri
BLOCK_WIDTH = int(GAME_AREA_WIDTH * 0.07)
BLOCK_HEIGHT = int(GAME_AREA_HEIGHT * 0.04)
BLOCK_COLS = min(12, int(GAME_AREA_WIDTH / (BLOCK_WIDTH + 5)))
BLOCK_ROWS = 6
BLOCK_SPACING = 5
BLOCK_OFFSET_X = GAME_AREA_X + (GAME_AREA_WIDTH - (BLOCK_COLS * (BLOCK_WIDTH + BLOCK_SPACING))) // 2
BLOCK_OFFSET_Y = GAME_AREA_Y + int(GAME_AREA_HEIGHT * 0.05)

# Bariyer tuğlaları
BARRIER_TILE_SIZE = 15
BARRIER_ROWS = 1

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.vx = random.uniform(-3, 3)
        self.vy = random.uniform(-5, -1)
        self.color = color
        self.life = 30
        self.size = random.randint(2, 5)
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.3
        self.life -= 1
        return self.life > 0
    
    def draw(self, screen):
        alpha = self.life / 30
        size = int(self.size * alpha)
        if size > 0:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), size)

class PowerUp:
    def __init__(self, x, y, power_type):
        self.radius = 15
        self.x = x
        self.y = y
        self.type = power_type
        self.active = True
        self.speed = 4
        self.animation_offset = 0
        self.rect = pygame.Rect(x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)
        self._font = pygame.font.Font(None, int(self.radius * 1.6))
        self._colors = {
            'B': COLORS['GREEN'],  'K': COLORS['BLUE'],   'X': COLORS['PURPLE'],
            'C': COLORS['RED'],    'O': COLORS['ORANGE'], 'H': COLORS['YELLOW'],
            'M': COLORS['CYAN'],   'Y': COLORS['PINK'],   'Z': COLORS['LIME'],
            'D': (60, 80, 220),    'T': COLORS['GOLD'],   'A': (220, 60, 0),
        }
        
    def update(self):
        self.y += self.speed
        self.rect.y = self.y - self.radius
        self.animation_offset += 0.1
        
    def draw(self, screen):
        if not self.active:
            return

        color = self._colors.get(self.type, COLORS['WHITE'])
        pulse = math.sin(self.animation_offset * 3.0) * 2.5
        r = int(self.radius + pulse)
        cx, cy = int(self.x), int(self.y)

        # Çok katmanlı dış glow (SRCALPHA yüzey)
        glow_size = r * 2 + 22
        gc = glow_size // 2
        glow_surf = pygame.Surface((glow_size, glow_size), pygame.SRCALPHA)
        for extra, alpha in [(10, 18), (7, 38), (4, 62), (2, 95)]:
            pygame.draw.circle(glow_surf, (*color, alpha), (gc, gc), r + extra)
        screen.blit(glow_surf, (cx - gc, cy - gc))

        # Koyu merkez + renkli dış kabuk (gem efekti)
        dark = tuple(max(0, c // 3) for c in color)
        pygame.draw.circle(screen, dark, (cx, cy), r)
        pygame.draw.circle(screen, color, (cx, cy), r, max(1, r // 3))

        # Parlak kenar halkası
        bright = tuple(min(255, c + 80) for c in color)
        pygame.draw.circle(screen, bright, (cx, cy), r, 2)

        # İnce beyaz dış çizgi
        pygame.draw.circle(screen, (210, 220, 255), (cx, cy), r + 1, 1)

        # Cam yansıması (sol üst)
        pygame.draw.circle(screen, (255, 255, 255), (cx - r // 4, cy - r // 4), max(1, r // 5))

        # Harf
        text = self._font.render(self.type, True, COLORS['WHITE'])
        screen.blit(text, text.get_rect(center=(cx, cy)))

class Effect:
    def __init__(self, effect_type, duration):
        self.type = effect_type
        self.duration = duration
        self.start_time = pygame.time.get_ticks()
        self.active = True
    
    def is_expired(self):
        return pygame.time.get_ticks() - self.start_time > self.duration
    
    def get_remaining(self, now=None):
        t = now if now is not None else pygame.time.get_ticks()
        return max(0, (self.duration - (t - self.start_time)) // 1000)
    
    def refresh(self):
        self.start_time = pygame.time.get_ticks()

class TrailEffect:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.life = 10
    
    def update(self):
        self.life -= 1
        return self.life > 0
    
    def draw(self, screen, radius, color):
        alpha = self.life / 10
        size = int(radius * alpha)
        if size > 0:
            pygame.draw.circle(screen, color, (int(self.x), int(self.y)), size)

class Bullet:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.radius = max(3, BALL_RADIUS // 2)
        self.speed_y = BALL_SPEED_Y * 2.5

    def update(self):
        self.y += self.speed_y
        return self.y - self.radius > GAME_AREA_Y

    def draw(self, screen):
        cx, cy = int(self.x), int(self.y)
        pygame.draw.circle(screen, (255, 80, 0), (cx, cy), self.radius)
        pygame.draw.circle(screen, (255, 210, 60), (cx, cy), max(1, self.radius - 1))

class Barrier:
    def __init__(self):
        self.tiles = []
        self.active = False
        self.start_time = 0
        self.duration = 0
    
    def activate(self, duration):
        self.active = True
        self.start_time = pygame.time.get_ticks()
        self.duration = duration
        self.create_tiles()
    
    def create_tiles(self):
        self.tiles = []
        start_x = GAME_AREA_X
        start_y = SCREEN_HEIGHT - BARRIER_TILE_SIZE - 4
        for row in range(BARRIER_ROWS):
            for col in range(int(GAME_AREA_WIDTH / BARRIER_TILE_SIZE) + 1):
                x = start_x + col * BARRIER_TILE_SIZE
                y = start_y + row * BARRIER_TILE_SIZE
                if x + BARRIER_TILE_SIZE <= GAME_AREA_X + GAME_AREA_WIDTH:
                    rect = pygame.Rect(x, y, BARRIER_TILE_SIZE - 1, BARRIER_TILE_SIZE - 1)
                    self.tiles.append(rect)
    
    def update(self):
        if self.active:
            if pygame.time.get_ticks() - self.start_time > self.duration:
                self.active = False
                self.tiles.clear()
    
    def draw(self, screen):
        if self.active:
            for tile in self.tiles:
                pygame.draw.rect(screen, (139, 69, 19), tile)
                pygame.draw.rect(screen, (101, 67, 33), tile, 1)
    
    def check_collision(self, ball):
        if not self.active:
            return False
        for tile in self.tiles:
            if ball.rect.colliderect(tile):
                return True
        return False

class Ball:
    def __init__(self, x=None, y=None, level=1, radius=None, sticky=False):
        self.radius = radius if radius is not None else BALL_RADIUS
        self.original_radius = BALL_RADIUS
        self.x = x if x is not None else GAME_AREA_X + GAME_AREA_WIDTH // 2
        self.y = y if y is not None else GAME_AREA_Y + GAME_AREA_HEIGHT - 100
        self.level = level
        self.update_speed_by_level()
        self.ghost_mode = False
        self.speed_boost = False
        self.big_mode = False
        self.sticky = sticky
        self.stuck_to_paddle = True
        self.original_speed_x = self.speed_x
        self.original_speed_y = self.speed_y
        self.trail_effects = []
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius,
                                self.radius * 2, self.radius * 2)
        self.active = True
        self.wall_hit = False
        self.sticky_cooldown = 0
    
    def update_speed_by_level(self):
        _level_multipliers = {1: 0.60, 2: 0.70, 3: 0.80, 4: 0.90, 5: 1.00,
                              6: 1.10, 7: 1.20, 8: 1.35, 9: 1.50, 10: 1.65}
        speed_multiplier = _level_multipliers.get(self.level, 1.0)
        
        self.speed_x = BALL_SPEED_X * speed_multiplier * random.choice([-1, 1])
        self.speed_y = BALL_SPEED_Y * speed_multiplier
        self.original_speed_x = self.speed_x
        self.original_speed_y = self.speed_y
    
    def update(self, paddle_rect=None):
        if not self.active:
            return
            
        if self.stuck_to_paddle and paddle_rect:
            self.x = paddle_rect.x + paddle_rect.width // 2
            self.y = paddle_rect.y - self.radius - 2
            self.rect.x = self.x - self.radius
            self.rect.y = self.y - self.radius
            return

        if self.sticky_cooldown > 0:
            self.sticky_cooldown -= 1

        if self.ghost_mode:
            self.trail_effects.append(TrailEffect(self.x, self.y))
            if len(self.trail_effects) > 20:
                self.trail_effects.pop(0)
        
        self.x += self.speed_x
        self.y += self.speed_y
        self.rect.x = self.x - self.radius
        self.rect.y = self.y - self.radius
        
        self.wall_hit = False
        if self.x - self.radius <= GAME_AREA_X:
            self.x = GAME_AREA_X + self.radius
            self.speed_x = abs(self.speed_x)
            self.wall_hit = True
        elif self.x + self.radius >= GAME_AREA_X + GAME_AREA_WIDTH:
            self.x = GAME_AREA_X + GAME_AREA_WIDTH - self.radius
            self.speed_x = -abs(self.speed_x)
            self.wall_hit = True

        if self.y - self.radius <= GAME_AREA_Y:
            self.y = GAME_AREA_Y + self.radius
            self.speed_y = abs(self.speed_y)
            self.wall_hit = True
    
    def launch(self):
        self.stuck_to_paddle = False
        if self.speed_x == 0 and self.speed_y == 0:
            spd = math.sqrt(self.original_speed_x ** 2 + self.original_speed_y ** 2)
            if spd == 0:
                spd = abs(BALL_SPEED_Y)
            self.speed_x = spd * random.uniform(-0.4, 0.4)
            self.speed_y = -spd * 0.92
        else:
            self.speed_x = self.original_speed_x
            self.speed_y = self.original_speed_y
        if self.sticky:
            self.sticky_cooldown = 75
    
    def draw(self, screen):
        if not self.active:
            return
            
        if self.ghost_mode:
            for trail in self.trail_effects[:]:
                if trail.update():
                    trail.draw(screen, self.radius, COLORS['PURPLE'])
                else:
                    self.trail_effects.remove(trail)
        
        if self.sticky:
            color = COLORS['GOLD']
            pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)
            pygame.draw.circle(screen, COLORS['ORANGE'], (int(self.x), int(self.y)), self.radius, 3)
        elif self.ghost_mode:
            color = COLORS['PURPLE']
            pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)
            pygame.draw.circle(screen, COLORS['WHITE'], (int(self.x), int(self.y)), self.radius, 2)
        elif self.big_mode:
            color = COLORS['LIME']
            pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)
            pygame.draw.circle(screen, COLORS['GOLD'], (int(self.x), int(self.y)), self.radius, 3)
        else:
            if self.speed_boost:
                color = COLORS['DARK_ORANGE']
            else:
                color = COLORS['WHITE']
            pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)
            pygame.draw.circle(screen, COLORS['YELLOW'], (int(self.x), int(self.y)), self.radius, 2)
        
        highlight_x = int(self.x - self.radius * 0.3)
        highlight_y = int(self.y - self.radius * 0.3)
        highlight_radius = max(1, self.radius // 3)
        pygame.draw.circle(screen, COLORS['WHITE'], (highlight_x, highlight_y), highlight_radius)
    
    def reset_position(self):
        self.x = GAME_AREA_X + GAME_AREA_WIDTH // 2
        self.y = GAME_AREA_Y + GAME_AREA_HEIGHT - 100
        self.update_speed_by_level()
        self.rect.x = self.x - self.radius
        self.rect.y = self.y - self.radius
        self.trail_effects.clear()
        self.stuck_to_paddle = True
    
    def set_speed_boost(self, active):
        self.speed_boost = active
        if active:
            sx = 1 if self.speed_x >= 0 else -1
            sy = 1 if self.speed_y >= 0 else -1
            self.speed_x = max(-MAX_BALL_SPEED, min(MAX_BALL_SPEED, sx * abs(self.original_speed_x) * 1.4))
            self.speed_y = max(-MAX_BALL_SPEED, min(MAX_BALL_SPEED, sy * abs(self.original_speed_y) * 1.4))
        else:
            sx = 1 if self.speed_x >= 0 else -1
            sy = 1 if self.speed_y >= 0 else -1
            self.speed_x = sx * abs(self.original_speed_x)
            self.speed_y = sy * abs(self.original_speed_y)
    
    def resize(self, new_radius):
        old_radius = self.radius
        self.radius = max(BALL_MIN_RADIUS, min(BALL_MAX_RADIUS, new_radius))
        self.rect.width = self.radius * 2
        self.rect.height = self.radius * 2
        if new_radius < self.original_radius:
            self.speed_x *= 1.2
            self.speed_y *= 1.2

    def reset_size(self):
        self.radius = self.original_radius
        self.big_mode = False
        self.rect.width = self.radius * 2
        self.rect.height = self.radius * 2
        sx = 1 if self.speed_x >= 0 else -1
        sy = 1 if self.speed_y >= 0 else -1
        self.speed_x = sx * abs(self.original_speed_x)
        self.speed_y = sy * abs(self.original_speed_y)

    def set_sticky(self, active):
        self.sticky = active

class Paddle:
    def __init__(self):
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.original_width = PADDLE_WIDTH
        self.x = GAME_AREA_X + GAME_AREA_WIDTH // 2 - self.width // 2
        self.y = GAME_AREA_Y + GAME_AREA_HEIGHT - self.height - BARRIER_TILE_SIZE - 25
        self.speed = PADDLE_SPEED
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.squish = 0          # piksel cinsinden aşağı kayma
        self.color_state = 'normal'  # 'normal' | 'big' | 'small' | 'sticky'
    
    def update(self, mouse_x=None):
        if mouse_x:
            self.x = mouse_x - self.width // 2
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.x > GAME_AREA_X:
                self.x -= self.speed
            if keys[pygame.K_RIGHT] and self.x < GAME_AREA_X + GAME_AREA_WIDTH - self.width:
                self.x += self.speed
        
        self.x = max(GAME_AREA_X, min(self.x, GAME_AREA_X + GAME_AREA_WIDTH - self.width))
        self.rect.x = self.x
        if self.squish > 0:
            self.squish = max(0, self.squish - 2)
    
    def resize(self, new_width):
        old_width = self.width
        self.width = max(PADDLE_MIN_WIDTH, min(PADDLE_MAX_WIDTH, new_width))
        self.x = self.x + (old_width - self.width) // 2
        self.x = max(GAME_AREA_X, min(self.x, GAME_AREA_X + GAME_AREA_WIDTH - self.width))
        self.rect.width = self.width
    
    def reset_size(self):
        self.width = PADDLE_WIDTH
        self.original_width = PADDLE_WIDTH
        self.x = GAME_AREA_X + GAME_AREA_WIDTH // 2 - self.width // 2
        self.rect.width = self.width
        self.rect.x = self.x
    
    def draw(self, screen):
        r = self.height // 2
        yy = self.y + self.squish   # squish: kısa süre aşağı kayar

        _states = {
            'big':    ((80, 200, 80),  (30, 120, 30),  COLORS['GREEN']),
            'small':  ((220, 70, 70),  (140, 30, 30),  COLORS['RED']),
            'sticky': ((210, 160, 10), (140, 100, 0),  COLORS['GOLD']),
            'fire':   ((220, 90, 0),   (140, 40, 0),   (255, 60, 0)),
            'normal': (COLORS['PADDLE_GRADIENT_TOP'],
                       COLORS['PADDLE_GRADIENT_BOTTOM'], COLORS['CYAN']),
        }
        top_c, bot_c, edge_c = _states.get(self.color_state, _states['normal'])

        # Kapsül gradyan dolgu — her satır huni şekline kırpılır
        r2 = r * r
        for i in range(self.height):
            ratio = i / max(1, self.height - 1)
            cr = int(top_c[0] * (1 - ratio) + bot_c[0] * ratio)
            cg = int(top_c[1] * (1 - ratio) + bot_c[1] * ratio)
            cb = int(top_c[2] * (1 - ratio) + bot_c[2] * ratio)
            dy = i - r
            x_off = int(math.sqrt(max(0, r2 - dy * dy))) if abs(dy) <= r else 0
            pygame.draw.line(screen, (cr, cg, cb),
                             (self.x + r - x_off, yy + i),
                             (self.x + self.width - r + x_off, yy + i))

        # Dış kenar (pygame 2.x border_radius desteği)
        pygame.draw.rect(screen, edge_c,
                         pygame.Rect(self.x, yy, self.width, self.height),
                         2, border_radius=r)

        # Üst iç ışık çizgisi
        bright = tuple(min(255, c + 80) for c in edge_c)
        pygame.draw.line(screen, bright,
                         (self.x + r + 4, yy + 2),
                         (self.x + self.width - r - 4, yy + 2), 2)

        # Topçu namluları — ateş modunda her iki uçta
        if self.color_state == 'fire':
            cannon_r = max(4, self.height // 2)
            for cx in (self.x + cannon_r, self.x + self.width - cannon_r):
                pygame.draw.circle(screen, (255, 80, 0), (cx, yy - cannon_r // 2), cannon_r)
                pygame.draw.circle(screen, (255, 200, 60), (cx, yy - cannon_r // 2), cannon_r, 2)
                pygame.draw.circle(screen, (255, 255, 140),
                                   (cx - 1, yy - cannon_r // 2 - 1), max(1, cannon_r // 3))
    
    def reset_position(self):
        self.x = GAME_AREA_X + GAME_AREA_WIDTH // 2 - self.width // 2
        self.y = GAME_AREA_Y + GAME_AREA_HEIGHT - self.height - BARRIER_TILE_SIZE - 25
        self.rect.x = self.x
        self.rect.y = self.y

class Block:
    def __init__(self, x, y, color, hits_required=1, indestructible=False):
        self.rect = pygame.Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)
        self.color = color
        self.hits_required = hits_required
        self.current_hits = 0
        self.active = True
        self.indestructible = indestructible
    
    def hit(self):
        if self.indestructible:
            return False
        self.current_hits += 1
        if self.current_hits >= self.hits_required:
            self.active = False
            return True
        return False
    
    def draw(self, screen):
        if self.active:
            if self.indestructible:
                pygame.draw.rect(screen, self.color, self.rect)
                pygame.draw.rect(screen, COLORS['DARK_RED'], self.rect, 3)
                pygame.draw.line(screen, COLORS['RED'], 
                               (self.rect.x + 10, self.rect.y + 10),
                               (self.rect.x + self.rect.width - 10, self.rect.y + self.rect.height - 10), 3)
                pygame.draw.line(screen, COLORS['RED'],
                               (self.rect.x + self.rect.width - 10, self.rect.y + 10),
                               (self.rect.x + 10, self.rect.y + self.rect.height - 10), 3)
            else:
                intensity = 1.0 - (self.current_hits / self.hits_required)
                r = min(255, int(self.color[0] * (0.3 + intensity * 0.7)))
                g = min(255, int(self.color[1] * (0.3 + intensity * 0.7)))
                b = min(255, int(self.color[2] * (0.3 + intensity * 0.7)))
                current_color = (r, g, b)
                pygame.draw.rect(screen, current_color, self.rect)
                pygame.draw.rect(screen, COLORS['WHITE'], self.rect, 2)

class Level:
    def __init__(self, level_number):
        self.level_number = level_number
        self.blocks = []
        self.create_blocks()
        self.background_color = LEVEL_BACKGROUNDS.get(level_number, COLORS['BLACK'])
        self._generate_stars()
    
    def create_blocks(self):
        self.blocks = []
        
        # İlk 3 bölümde siyah tuğla yok
        if self.level_number >= 4:
            wall_count = 3 if self.level_number >= 8 else (2 if self.level_number >= 6 else 1)
        else:
            wall_count = 0
        
        wall_positions = []
        if wall_count > 0:
            available_positions = list(range(BLOCK_COLS))
            random.shuffle(available_positions)
            wall_positions = available_positions[:wall_count]
        
        for row in range(BLOCK_ROWS):
            for col in range(BLOCK_COLS):
                x = BLOCK_OFFSET_X + col * (BLOCK_WIDTH + BLOCK_SPACING)
                y = BLOCK_OFFSET_Y + row * (BLOCK_HEIGHT + BLOCK_SPACING)
                
                is_wall = (row == BLOCK_ROWS - 1 and col in wall_positions)
                
                if is_wall:
                    block = Block(x, y, COLORS['INDESTRUCTIBLE'], 999, True)
                    self.blocks.append(block)
                    continue
                
                if self.level_number >= 8 and row >= 3:
                    hits = 3
                    color = COLORS['DARK_RED']
                elif self.level_number >= 6 and row >= 3:
                    hits = 2
                    color = COLORS['ORANGE']
                elif self.level_number >= 4 and row >= 2:
                    hits = 2
                    color = self.get_block_color(row)
                else:
                    hits = 1
                    color = self.get_block_color(row)
                
                block = Block(x, y, color, hits, False)
                self.blocks.append(block)
    
    def _generate_stars(self):
        self.stars = []
        num_stars = 130 + self.level_number * 10
        for _ in range(num_stars):
            x = random.randint(GAME_AREA_X, GAME_AREA_X + GAME_AREA_WIDTH - 1)
            y = random.randint(GAME_AREA_Y, SCREEN_HEIGHT - 1)
            size = random.choices([1, 2, 3], weights=[70, 25, 5])[0]
            base_brightness = random.randint(100, 240)
            twinkle_speed = random.uniform(0.4, 3.0)
            twinkle_phase = random.uniform(0, 6.28)
            self.stars.append((x, y, size, base_brightness, twinkle_speed, twinkle_phase))

    def get_block_color(self, row):
        colors = [COLORS['RED'], COLORS['ORANGE'], COLORS['YELLOW'], COLORS['GREEN'], COLORS['CYAN'], COLORS['PURPLE']]
        shift = (self.level_number - 1) % len(colors)
        return colors[(row + shift) % len(colors)]
    
    def draw(self, screen):
        # Çok koyu, hafif bölüm rengi tonlu arka zemin
        r = max(0, self.background_color[0] // 7)
        g = max(0, self.background_color[1] // 7)
        b = max(5, self.background_color[2] // 5)
        screen.fill((r, g, b))

        # Titreşen yıldızlar
        t = pygame.time.get_ticks() / 1000.0
        for (sx, sy, size, base_b, speed, phase) in self.stars:
            brightness = int(base_b + math.sin(t * speed + phase) * 40)
            brightness = max(50, min(255, brightness))
            color = (brightness, brightness, brightness)
            if size == 1:
                screen.set_at((sx, sy), color)
            else:
                pygame.draw.circle(screen, color, (sx, sy), size)

        for block in self.blocks:
            block.draw(screen)
    
    def all_blocks_destroyed(self):
        destructible_blocks = [b for b in self.blocks if not b.indestructible]
        return all(not block.active for block in destructible_blocks)

class HighScore:
    def __init__(self):
        self.scores = []
        _base = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(_base, "highscores.json")
        self.load_scores()
    
    def load_scores(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    self.scores = json.load(f)
            except:
                self.scores = []
        if not self.scores:
            self.scores = []
    
    def save_scores(self):
        lock_path = self.filename + '.lock'
        deadline = time.time() + 5
        while os.path.exists(lock_path) and time.time() < deadline:
            time.sleep(0.05)
        try:
            with open(lock_path, 'w') as f:
                f.write('locked')
            # Başka bir kullanıcı bu arada yeni skor eklemiş olabilir, tekrar yükle
            self.load_scores()
            if hasattr(self, '_pending'):
                self.scores.append(self._pending)
                self.scores.sort(key=lambda x: x['score'], reverse=True)
                self.scores = self.scores[:10]
                del self._pending
            with open(self.filename, 'w') as f:
                json.dump(self.scores[:10], f)
        except Exception:
            pass
        finally:
            if os.path.exists(lock_path):
                try:
                    os.remove(lock_path)
                except Exception:
                    pass
    
    def add_score(self, name, score, level):
        self._pending = {
            "name": name.upper()[:15],
            "score": score,
            "level": level,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        self.save_scores()
    
    def is_high_score(self, score):
        return len(self.scores) < 10 or score >= self.scores[-1]['score']
    
    def get_rank(self, score):
        for i, s in enumerate(self.scores):
            if score >= s['score']:
                return i + 1
        return len(self.scores) + 1

class Settings:
    _DIR  = os.path.join(os.environ.get('APPDATA', os.path.expanduser('~')), 'PyBall')
    _FILE = os.path.join(_DIR, 'settings.json')
    FPS_OPTS = [60, 120, 144, 240]

    def __init__(self):
        self.sfx_vol   = 1.0
        self.music_vol = 0.35
        self.fps       = 60
        self.lang      = 'tr'
        os.makedirs(self._DIR, exist_ok=True)
        self._load()

    def _load(self):
        if not os.path.exists(self._FILE):
            return
        try:
            with open(self._FILE) as f:
                d = json.load(f)
            self.sfx_vol   = float(d.get('sfx_vol',   self.sfx_vol))
            self.music_vol = float(d.get('music_vol', self.music_vol))
            fps = int(d.get('fps', self.fps))
            self.fps  = fps if fps in self.FPS_OPTS else 60
            lang      = d.get('lang', 'tr')
            self.lang = lang if lang in ('tr', 'en') else 'tr'
        except Exception:
            pass
        LANG['current'] = self.lang

    def save(self):
        try:
            with open(self._FILE, 'w') as f:
                json.dump({'sfx_vol': self.sfx_vol,
                           'music_vol': self.music_vol,
                           'fps': self.fps,
                           'lang': self.lang}, f)
        except Exception:
            pass


class SoundManager:
    """Numpy gerektirmez — Python standart kütüphanesi + pygame yeterli."""

    _TWO_PI = 2 * math.pi
    _SR = 44100

    def __init__(self):
        self.enabled = False
        self.sounds = {}
        self._music = None
        try:
            self._build_sfx()
            self._build_music()
            self.enabled = True
        except Exception as e:
            print(f"[SoundManager] ses başlatılamadı: {e}")

    # ------------------------------------------------------------------ yardımcı
    @staticmethod
    def _make_sound(samples):
        """Float listesini [-1,1] aralığında alır, Sound nesnesi döner."""
        import array as _arr
        buf = _arr.array('h', (max(-32768, min(32767, int(s * 32767))) for s in samples))
        return pygame.mixer.Sound(buffer=buf)

    @classmethod
    def _tone(cls, freq, dur, vol=0.7, decay=20):
        """Tek frekans, üstel azalan zarf, liste döner."""
        n = int(cls._SR * dur)
        step = cls._TWO_PI * freq / cls._SR
        decay_k = math.exp(-decay / cls._SR)  # çarpımsal zarf (exp içten çıkar)
        env = 1.0
        result = []
        for i in range(n):
            result.append(math.sin(step * i) * env * vol)
            env *= decay_k
        return result

    @staticmethod
    def _mix2(a, b):
        return [x + y for x, y in zip(a, b)]

    @staticmethod
    def _cat(*lists):
        out = []
        for lst in lists:
            out += lst
        return out

    # ------------------------------------------------------------------ SFX
    def _build_sfx(self):
        sr = self._SR

        # Paddle: frekans sweep (500→200 Hz)
        n = int(sr * 0.05)
        phase = 0.0
        sweep = []
        for i in range(n):
            freq = 500 - 300 * i / n
            phase += self._TWO_PI * freq / sr
            sweep.append(math.sin(phase) * (1 - i / n) * 0.8)
        self.sounds['paddle'] = self._make_sound(sweep)

        self.sounds['wall']          = self._make_sound(self._tone(380, 0.07, 0.45, 25))
        self.sounds['block_hit']     = self._make_sound(self._mix2(
                                           self._tone(200, 0.07, 0.35, 30),
                                           self._tone(160, 0.07, 0.25, 30)))
        self.sounds['block_destroy'] = self._make_sound(self._mix2(
                                           self._tone(580, 0.09, 0.50, 22),
                                           self._tone(380, 0.09, 0.40, 18)))
        self.sounds['powerup']       = self._make_sound(self._cat(
                                           self._tone(262, 0.055, 0.6, 18),
                                           self._tone(330, 0.055, 0.6, 18),
                                           self._tone(392, 0.055, 0.6, 18),
                                           self._tone(523, 0.12,  0.7, 14)))
        self.sounds['life_lost']     = self._make_sound(self._cat(
                                           self._tone(440, 0.12, 0.7, 12),
                                           self._tone(330, 0.12, 0.7, 12),
                                           self._tone(220, 0.22, 0.7, 10)))
        self.sounds['level_complete']= self._make_sound(self._cat(
                                           self._tone(262, 0.07, 0.7, 18),
                                           self._tone(330, 0.07, 0.7, 18),
                                           self._tone(392, 0.07, 0.7, 18),
                                           self._tone(523, 0.07, 0.7, 18),
                                           self._tone(659, 0.22, 0.8, 12)))
        self.sounds['game_over']     = self._make_sound(self._cat(
                                           self._tone(330, 0.13, 0.8, 14),
                                           self._tone(277, 0.13, 0.8, 14),
                                           self._tone(247, 0.13, 0.8, 14),
                                           self._tone(220, 0.13, 0.8, 14),
                                           self._tone(185, 0.35, 0.8, 10)))

    # ------------------------------------------------------------------ müzik
    def _build_music(self):
        sr = self._SR
        beat = 60 / 128          # 128 BPM → ~0.469 sn/beat
        n_beats = 8
        total = int(sr * beat * n_beats)
        music = [0.0] * total

        # Bas vuruş (her beat, La1=55 Hz + 110 Hz)
        k55  = math.exp(-10 / sr)
        k110 = math.exp(-10 / sr)
        for i in range(n_beats):
            s  = int(i * beat * sr)
            nb = min(int(beat * 0.6 * sr), total - s)
            e55 = e110 = 1.0
            for j in range(nb):
                t = j / sr
                music[s + j] += math.sin(self._TWO_PI * 55  * t) * e55  * 0.28
                music[s + j] += math.sin(self._TWO_PI * 110 * t) * e110 * 0.12
                e55  *= k55
                e110 *= k110

        # Arpej: La minör pentatonik
        for i, f in enumerate([220, 262, 330, 392, 440, 392, 330, 262]):
            s  = int(i * beat * sr)
            nb = min(int(beat * 0.42 * sr), total - s)
            step = self._TWO_PI * f / sr
            for j in range(nb):
                env = math.sin(math.pi * j / nb)
                music[s + j] += math.sin(step * j) * env * 0.13

        # Tiz vurgu (her 2 beat, La5=880 Hz)
        k880 = math.exp(-35 / sr)
        for i in [0, 2, 4, 6]:
            s  = int(i * beat * sr)
            nb = min(int(beat * 0.12 * sr), total - s)
            e = 1.0
            for j in range(nb):
                music[s + j] += math.sin(self._TWO_PI * 880 * j / sr) * e * 0.08
                e *= k880

        self._music = self._make_sound(music)
        self._music.set_volume(0.35)

    # ------------------------------------------------------------------ API
    def play(self, name):
        if self.enabled and name in self.sounds:
            self.sounds[name].play()

    def start_music(self):
        if self.enabled and self._music:
            self._music.play(-1)

    def stop_music(self):
        if self.enabled and self._music:
            self._music.stop()

    def set_sfx_volume(self, vol):
        for snd in self.sounds.values():
            snd.set_volume(vol)

    def set_music_volume(self, vol):
        if self._music:
            self._music.set_volume(vol)


class Menu:
    _ITEM_COLORS = [
        (0, 230, 118),
        (255, 214, 0),
        (100, 181, 246),
        (206, 147, 216),
        (239, 83, 80),
    ]

    def __init__(self, screen):
        self.screen      = screen
        self.options     = ['menu_start', 'menu_highscores', 'menu_howtoplay', 'menu_settings', 'menu_exit']
        self.selected    = 0
        self.title_font  = pygame.font.Font(None, int(SCREEN_HEIGHT * 0.13))
        self.btn_font    = pygame.font.Font(None, int(SCREEN_HEIGHT * 0.055))
        self.sub_font    = pygame.font.Font(None, int(SCREEN_HEIGHT * 0.038))
        self.hint_font   = pygame.font.Font(None, int(SCREEN_HEIGHT * 0.028))
        self.stars       = self._gen_stars(200)
        self.deco_blocks = self._gen_deco()
        self._demo = {
            'bx': float(SCREEN_WIDTH // 2),
            'by': float(SCREEN_HEIGHT * 0.55),
            'vx': 3.5, 'vy': -2.8,
            'px': float(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2),
            '_last_t': pygame.time.get_ticks(),
        }

    @staticmethod
    def _gen_stars(n):
        out = []
        for _ in range(n):
            x  = random.randint(0, SCREEN_WIDTH - 1)
            y  = random.randint(0, SCREEN_HEIGHT - 1)
            sz = random.choices([1, 2, 3], weights=[70, 25, 5])[0]
            bb = random.randint(80, 220)
            sp = random.uniform(0.3, 2.5)
            ph = random.uniform(0, 6.28)
            out.append((x, y, sz, bb, sp, ph))
        return out

    @staticmethod
    def _gen_deco():
        palette = [
            (255, 80, 80), (255, 170, 0), (255, 230, 0),
            (60, 220, 80), (60, 180, 255), (180, 80, 255),
        ]
        blocks = []
        for row in range(4):
            for col in range(BLOCK_COLS):
                x = BLOCK_OFFSET_X + col * (BLOCK_WIDTH + BLOCK_SPACING)
                y = BLOCK_OFFSET_Y + row * (BLOCK_HEIGHT + BLOCK_SPACING)
                c = palette[(row * 3 + col) % len(palette)]
                blocks.append((x, y, c))
        return blocks

    def _update_demo(self):
        d   = self._demo
        now = pygame.time.get_ticks()
        dt  = min((now - d['_last_t']) / (1000.0 / 60), 4.0)
        d['_last_t'] = now
        br  = BALL_RADIUS + 2

        d['bx'] += d['vx'] * dt
        d['by'] += d['vy'] * dt

        if   d['bx'] - br < 0:             d['bx'] = float(br);                  d['vx'] =  abs(d['vx'])
        elif d['bx'] + br > SCREEN_WIDTH:   d['bx'] = float(SCREEN_WIDTH  - br);  d['vx'] = -abs(d['vx'])
        if   d['by'] - br < 0:             d['by'] = float(br);                  d['vy'] =  abs(d['vy'])
        elif d['by'] + br > SCREEN_HEIGHT:  d['by'] = float(SCREEN_HEIGHT - br);  d['vy'] = -abs(d['vy'])

        target   = d['bx'] - PADDLE_WIDTH // 2
        d['px'] += (target - d['px']) * 0.04 * dt

    def draw(self):
        s = self.screen
        t = pygame.time.get_ticks() / 1000.0

        # --- Arka zemin
        s.fill((8, 8, 28))

        # --- Yıldız alanı
        for (sx, sy, sz, bb, sp, ph) in self.stars:
            b = max(40, min(255, int(bb + math.sin(t * sp + ph) * 35)))
            if sz == 1:
                s.set_at((sx, sy), (b, b, b))
            else:
                pygame.draw.circle(s, (b, b, b), (sx, sy), sz)

        # --- Dekoratif bloklar (yarı saydam, titreşimli)
        deco_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        for idx, (bx, by, bc) in enumerate(self.deco_blocks):
            a = int((math.sin(t * 1.5 + idx * 0.4) * 0.3 + 0.45) * 160)
            pygame.draw.rect(deco_surf, (*bc, a),
                             pygame.Rect(bx, by, BLOCK_WIDTH, BLOCK_HEIGHT), border_radius=4)
            pygame.draw.rect(deco_surf, (255, 255, 255, int(a * 0.4)),
                             pygame.Rect(bx, by, BLOCK_WIDTH, BLOCK_HEIGHT), 2, border_radius=4)
        s.blit(deco_surf, (0, 0))

        # --- Arka planda gezinen top + paddle (çok soluk)
        self._update_demo()
        d = self._demo
        demo_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        pr = pygame.Rect(int(d['px']), int(SCREEN_HEIGHT * 0.82), PADDLE_WIDTH, PADDLE_HEIGHT)
        pygame.draw.rect(demo_surf,   (120, 140, 200, 22), pr, border_radius=PADDLE_HEIGHT // 2)
        pygame.draw.circle(demo_surf, (180, 200, 255, 22),
                           (int(d['bx']), int(d['by'])), BALL_RADIUS + 2)
        s.blit(demo_surf, (0, 0))

        # --- Neon başlık "PYBREAKOUT"
        title_cx = SCREEN_WIDTH // 2
        title_cy = int(SCREEN_HEIGHT * 0.25)
        pb       = int(math.sin(t * 2.0) * 30 + 200)
        glow_col = (pb, int(pb * 0.85), 0)
        for off, a in [(7, 22), (4, 45), (2, 75)]:
            for ddx, ddy in [(-off, 0), (off, 0), (0, -off), (0, off)]:
                gt = self.title_font.render("PyBall", True, glow_col)
                gt.set_alpha(a)
                s.blit(gt, gt.get_rect(center=(title_cx + ddx, title_cy + ddy)))
        bright = (min(255, pb + 55), min(255, int((pb + 55) * 0.85)), 0)
        ts = self.title_font.render("PyBall", True, bright)
        s.blit(ts, ts.get_rect(center=(title_cx, title_cy)))

        # --- Alt başlık
        sub = self.sub_font.render(T('menu_subtitle'), True, COLORS['SILVER'])
        s.blit(sub, sub.get_rect(center=(SCREEN_WIDTH // 2, title_cy + int(SCREEN_HEIGHT * 0.10))))

        # --- Ayırıcı çizgi
        sep_y = int(SCREEN_HEIGHT * 0.40)
        lw    = int(SCREEN_WIDTH  * 0.40)
        lx    = SCREEN_WIDTH // 2 - lw // 2
        pygame.draw.line(s, (50,  50,  130), (lx,      sep_y),     (lx + lw,      sep_y),     1)
        pygame.draw.line(s, (130, 130, 230), (lx + 20, sep_y - 1), (lx + lw - 20, sep_y - 1), 1)

        # --- Menü düğmeleri
        btn_w = int(SCREEN_WIDTH  * 0.40)
        btn_h = int(SCREEN_HEIGHT * 0.08)
        btn_x = SCREEN_WIDTH // 2 - btn_w // 2
        by0   = int(SCREEN_HEIGHT * 0.43)
        bgap  = btn_h + int(SCREEN_HEIGHT * 0.016)
        br2   = btn_h // 2

        for i, option in enumerate(self.options):
            by2 = by0 + i * bgap
            sel = (i == self.selected)
            ic  = self._ITEM_COLORS[i]

            btn_surf = pygame.Surface((btn_w, btn_h), pygame.SRCALPHA)
            if sel:
                bg_a = int(math.sin(t * 4) * 15 + 140)
                pygame.draw.rect(btn_surf, (*ic, bg_a), (0, 0, btn_w, btn_h), border_radius=br2)
                pygame.draw.rect(btn_surf, (*ic, 255),  (0, 0, btn_w, btn_h), 2, border_radius=br2)
                pygame.draw.rect(btn_surf, (255, 255, 255, 35),
                                 (4, 4, btn_w - 8, btn_h // 2 - 2), border_radius=br2)
            else:
                pygame.draw.rect(btn_surf, (20, 20, 50, 155), (0, 0, btn_w, btn_h), border_radius=br2)
                pygame.draw.rect(btn_surf, (*ic, 75),   (0, 0, btn_w, btn_h), 1, border_radius=br2)
            s.blit(btn_surf, (btn_x, by2))

            mr = btn_h // 4
            mx = btn_x + btn_h // 2
            my = by2  + btn_h // 2
            if sel:
                pygame.draw.circle(s, ic, (mx, my), mr)
                pygame.draw.circle(s, (255, 255, 255), (mx, my), mr, 1)
            else:
                pygame.draw.circle(s, ic, (mx, my), mr, 2)

            txt_col = (255, 255, 255) if sel else (180, 180, 215)
            txt = self.btn_font.render(T(option), True, txt_col)
            s.blit(txt, txt.get_rect(midleft=(btn_x + btn_h + 4, by2 + btn_h // 2)))

        # --- Alt ipucu
        hint = self.hint_font.render(T('menu_hint'), True, (90, 90, 150))
        s.blit(hint, hint.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - int(SCREEN_HEIGHT * 0.04))))

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                return self.options[self.selected]
        return None

def draw_frame(screen):
    # Neon glow: dıştan içe, karanlıktan parlağa doğru 8 katman
    layers = [
        (0, (15,  15,  50)),
        (1, (35,  40, 100)),
        (2, (80,  90, 180)),
        (3, (150, 165, 235)),
        (4, (160, 175, 245)),
        (5, (85,  100, 190)),
        (6, (40,  48,  120)),
        (7, (20,  24,   70)),
    ]
    for i, color in layers:
        pygame.draw.line(screen, color, (i, i), (SCREEN_WIDTH - i - 1, i))             # üst
        pygame.draw.line(screen, color, (i, i), (i, SCREEN_HEIGHT - 1))                # sol
        pygame.draw.line(screen, color, (SCREEN_WIDTH - i - 1, i),
                         (SCREEN_WIDTH - i - 1, SCREEN_HEIGHT - 1))                    # sağ
    # İç kenar glow çizgisi (sol/üst/sağ, alt yok)
    inner = (45, 52, 115)
    pygame.draw.line(screen, inner, (FRAME_THICKNESS, FRAME_THICKNESS),
                     (SCREEN_WIDTH - FRAME_THICKNESS, FRAME_THICKNESS))
    pygame.draw.line(screen, inner, (FRAME_THICKNESS, FRAME_THICKNESS),
                     (FRAME_THICKNESS, SCREEN_HEIGHT - 1))
    pygame.draw.line(screen, inner, (SCREEN_WIDTH - FRAME_THICKNESS, FRAME_THICKNESS),
                     (SCREEN_WIDTH - FRAME_THICKNESS, SCREEN_HEIGHT - 1))

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),
                                               pygame.FULLSCREEN | pygame.DOUBLEBUF)
        pygame.display.set_caption("PyBall - Breakout Şampiyonu")
        _base     = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
        _ico_path = os.path.join(_base, "PyBall.ico")
        if os.path.exists(_ico_path):
            pygame.display.set_icon(pygame.image.load(_ico_path))
        self.clock = pygame.time.Clock()
        self.menu = Menu(self.screen)
        self.high_score = HighScore()
        self.state = "MENU"
        self.how_to_play_text = None
        
        self.title_font = pygame.font.Font(None, int(SCREEN_HEIGHT * 0.07))
        self.font = pygame.font.Font(None, int(SCREEN_HEIGHT * 0.05))
        self.small_font = pygame.font.Font(None, int(SCREEN_HEIGHT * 0.025))
        self.tiny_font = pygame.font.Font(None, int(SCREEN_HEIGHT * 0.02))
        
        self.paddle = Paddle()
        self.balls = []
        self.barrier = Barrier()
        
        self.current_level = 1
        self.level = None
        self.score = 0
        self.lives = 3
        self.running = True
        self.game_over = False
        self.level_complete = False
        self.show_name_input = False
        self.show_help = False
        self.paused = False
        self.waiting_for_launch = True
        self.player_name = ""
        self.final_score = 0
        
        self.powerups = []
        self.active_effects = []
        self.particles = []
        self.bullets = []
        self._fire_timer = 0

        self.heart_powerup_count = 0
        self.max_heart_powerups = 5
        
        self.mouse_control = True
        self.mouse_x = GAME_AREA_X + GAME_AREA_WIDTH // 2
        
        self.powerup_drop_chance = 0.08
        
        self.blocks_destroyed = 0
        self.powerups_collected = 0
        self.start_time = pygame.time.get_ticks()
        self.settings = Settings()   # LANG['current'] burada ayarlanır
        self.create_how_to_play_text()
        self.settings_selected = 0
        self.sound = SoundManager()
        self.sound.set_sfx_volume(self.settings.sfx_vol)
        self.sound.set_music_volume(self.settings.music_vol)
        self.screen_title_font = pygame.font.Font(None, int(SCREEN_HEIGHT * 0.09))
        self._bg_stars         = Menu._gen_stars(150)
        self._effects_paused_at = 0

    def create_how_to_play_text(self):
        if LANG['current'] == 'tr':
            self.how_to_play_text = [
                "Nasıl Oynanır?",
                "",
                "  www.FreewareTR.com",
                "  youtube.com/CaprazBilgi",
                "",
                "Kontroller:",
                "← → / Fare: Paddle'ı hareket ettir",
                "Space / Mouse Click: Topu fırlat",
                "M: Fare/Klavye kontrolü geçişi",
                "F1: Yardım ekranı",
                "Esc: Menüye dön",
                "",
                "Güçlendirmeler (30 saniye):",
                "B (Yeşil): Paddle büyütür",
                "K (Mavi): Paddle küçültür",
                "X (Mor): Hayalet top (blokları kırarak geçer, siyah bloklara çarpar)",
                "C (Kırmızı): +1 Can (max 5)",
                "O (Turuncu): -1 Can",
                "H (Sarı): Top hızlanır",
                "M (Camgöbeği): Top küçülür + Hızlanır (%20)",
                "Y (Pembe): Top sayısı 3'e çıkar",
                "Z (Açık yeşil): Top büyür + 5 tuğla kırar + Duvara çarpınca alan hasarı",
                "D (Mavi): Tuğla bariyer (top alta düşmez)",
                "T (Altın): Yapışkan top (paddle'a yapışır)",
                "A (Turuncu-Kırmızı): Ateş modu — Paddle cannon şekli alır, Tıkla/Space: mermi fırlat",
                "",
                "Özel Bloklar:",
                "Çarpılı Siyah Bloklar: Kırılmaz, üst bölgeye geçişi engeller (4. bölümden itibaren)",
                "",
                "Zorluk Seviyeleri:",
                "Bölüm 1-3: Normal hız, siyah blok yok",
                "Bölüm 4-7: Orta hız + siyah bloklar",
                "Bölüm 8-10: Yüksek hız + çok siyah blok",
                "",
                "Menüye dönmek için Esc'ye basın",
            ]
        else:
            self.how_to_play_text = [
                "How to Play?",
                "",
                "  www.FreewareTR.com",
                "  youtube.com/CaprazBilgi",
                "",
                "Controls:",
                "← → / Mouse: Move the paddle",
                "Space / Mouse Click: Launch ball",
                "M: Toggle mouse/keyboard control",
                "F1: Help screen",
                "Esc: Return to menu",
                "",
                "Power-ups (30 seconds):",
                "B (Green): Enlarge paddle",
                "K (Blue): Shrink paddle",
                "X (Purple): Ghost ball (passes through blocks, hits black ones)",
                "C (Red): +1 Life (max 5)",
                "O (Orange): -1 Life",
                "H (Yellow): Speed up ball",
                "M (Cyan): Shrink ball + Speed up (20%)",
                "Y (Pink): Ball count increases to 3",
                "Z (Lime): Big ball + destroys 5 bricks + area damage on wall hit",
                "D (Blue): Brick barrier (ball won't fall through)",
                "T (Gold): Sticky ball (attaches to paddle)",
                "A (Orange-Red): Fire mode — Paddle becomes cannon, Click/Space: shoot",
                "",
                "Special Blocks:",
                "Crossed Black Blocks: Indestructible, blocks passage to upper area (from level 4)",
                "",
                "Difficulty Levels:",
                "Level 1-3: Normal speed, no black blocks",
                "Level 4-7: Medium speed + black blocks",
                "Level 8-10: High speed + many black blocks",
                "",
                "Press ESC to return to menu",
            ]
    
    def _draw_themed_bg(self, title_str, title_color=None):
        """Yıldız alanı + neon başlık + ayırıcı — tüm tema ekranlarında ortak zemin."""
        s = self.screen
        t = pygame.time.get_ticks() / 1000.0
        if title_color is None:
            title_color = COLORS['GOLD']

        s.fill((8, 8, 28))

        for (sx, sy, sz, bb, sp, ph) in self._bg_stars:
            b = max(40, min(255, int(bb + math.sin(t * sp + ph) * 35)))
            if sz == 1:
                s.set_at((sx, sy), (b, b, b))
            else:
                pygame.draw.circle(s, (b, b, b), (sx, sy), sz)

        title_cx = SCREEN_WIDTH // 2
        title_cy = int(SCREEN_HEIGHT * 0.09)
        pb       = int(math.sin(t * 2.0) * 20 + 200)
        scale    = pb / 220.0
        glow_col = tuple(min(255, int(c * scale)) for c in title_color)
        for off, a in [(5, 20), (3, 40), (1, 70)]:
            for ddx, ddy in [(-off, 0), (off, 0), (0, -off), (0, off)]:
                gt = self.screen_title_font.render(title_str, True, glow_col)
                gt.set_alpha(a)
                s.blit(gt, gt.get_rect(center=(title_cx + ddx, title_cy + ddy)))
        ts = self.screen_title_font.render(title_str, True, title_color)
        s.blit(ts, ts.get_rect(center=(title_cx, title_cy)))

        sep_y = int(SCREEN_HEIGHT * 0.15)
        lw    = int(SCREEN_WIDTH  * 0.55)
        lx    = SCREEN_WIDTH // 2 - lw // 2
        pygame.draw.line(s, (50, 50, 130),   (lx,      sep_y),     (lx + lw,      sep_y),     1)
        pygame.draw.line(s, (130, 130, 230), (lx + 20, sep_y - 1), (lx + lw - 20, sep_y - 1), 1)

    def draw_settings_screen(self):
        self._draw_themed_bg(T('settings_title'), (206, 147, 216))
        s = self.screen
        t = pygame.time.get_ticks() / 1000.0

        labels     = [T('sfx_label'), T('music_label'), T('fps_label'), T('lang_label')]
        values     = [
            f"%{int(self.settings.sfx_vol * 100)}",
            f"%{int(self.settings.music_vol * 100)}",
            str(self.settings.fps),
            T('lang_value'),
        ]
        volumes    = [self.settings.sfx_vol, self.settings.music_vol, None, None]
        row_colors = [(0, 230, 118), (100, 181, 246), (206, 147, 216), (255, 180, 50)]

        panel_w = int(SCREEN_WIDTH  * 0.65)
        panel_x = SCREEN_WIDTH // 2 - panel_w // 2
        row_h   = int(SCREEN_HEIGHT * 0.10)
        row_y0  = int(SCREEN_HEIGHT * 0.28)
        row_gap = row_h + int(SCREEN_HEIGHT * 0.03)
        br2     = row_h // 2

        for i, (lbl, val, vol) in enumerate(zip(labels, values, volumes)):
            ry  = row_y0 + i * row_gap
            sel = (self.settings_selected == i)
            ic  = row_colors[i]

            row_surf = pygame.Surface((panel_w, row_h), pygame.SRCALPHA)
            if sel:
                bg_a = int(math.sin(t * 4) * 15 + 130)
                pygame.draw.rect(row_surf, (*ic, bg_a), (0, 0, panel_w, row_h), border_radius=br2)
                pygame.draw.rect(row_surf, (*ic, 220),  (0, 0, panel_w, row_h), 2, border_radius=br2)
                pygame.draw.rect(row_surf, (255, 255, 255, 30),
                                 (4, 4, panel_w - 8, row_h // 2 - 2), border_radius=br2)
            else:
                pygame.draw.rect(row_surf, (20, 20, 55, 150), (0, 0, panel_w, row_h), border_radius=br2)
                pygame.draw.rect(row_surf, (*ic, 65),   (0, 0, panel_w, row_h), 1, border_radius=br2)
            s.blit(row_surf, (panel_x, ry))

            col = COLORS['WHITE'] if sel else (180, 180, 215)
            ty  = ry + row_h // 2 - self.font.get_height() // 2
            s.blit(self.font.render(lbl, True, col), (panel_x + row_h, ty))

            arrow_col = ic if sel else (70, 70, 120)
            val_cx    = panel_x + int(panel_w * 0.60)
            s.blit(self.font.render("◄", True, arrow_col), (val_cx,       ty))
            s.blit(self.font.render(val,  True, COLORS['WHITE']), (val_cx + 42,  ty))
            s.blit(self.font.render("►", True, arrow_col), (val_cx + 110, ty))

            if vol is not None:
                bx2 = val_cx + 162
                bw  = int(panel_w * 0.20)
                by2 = ry + row_h // 2 - 11
                bh  = 22
                pygame.draw.rect(s, (25, 25, 55), (bx2, by2, bw, bh), border_radius=11)
                bar_col = ic if sel else (55, 55, 90)
                pygame.draw.rect(s, bar_col, (bx2, by2, int(bw * vol), bh), border_radius=11)
                pygame.draw.rect(s, (90, 90, 160), (bx2, by2, bw, bh), 1, border_radius=11)

        hint = self.small_font.render(T('settings_hint'), True, (90, 90, 150))
        s.blit(hint, hint.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - int(SCREEN_HEIGHT * 0.05))))

    def _settings_adjust(self, direction):
        s = self.settings
        if self.settings_selected == 0:
            s.sfx_vol = round(max(0.0, min(1.0, s.sfx_vol + direction * 0.1)), 1)
            self.sound.set_sfx_volume(s.sfx_vol)
        elif self.settings_selected == 1:
            s.music_vol = round(max(0.0, min(1.0, s.music_vol + direction * 0.1)), 1)
            self.sound.set_music_volume(s.music_vol)
        elif self.settings_selected == 2:
            opts = Settings.FPS_OPTS
            idx = opts.index(s.fps) if s.fps in opts else 0
            s.fps = opts[(idx + direction) % len(opts)]
        elif self.settings_selected == 3:
            s.lang = 'en' if s.lang == 'tr' else 'tr'
            LANG['current'] = s.lang
            self.create_how_to_play_text()

    def draw_high_scores_screen(self):
        self._draw_themed_bg(T('menu_highscores'), COLORS['GOLD'])
        s = self.screen

        content_y = int(SCREEN_HEIGHT * 0.19)

        if not self.high_score.scores:
            no_score = self.font.render(T('hs_empty'), True, COLORS['SILVER'])
            s.blit(no_score, no_score.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
        else:
            col_x   = [int(SCREEN_WIDTH * r) for r in [0.08, 0.15, 0.42, 0.60, 0.74]]
            headers = ["#", T('hs_col_name'), T('hs_col_score'), T('hs_col_level'), T('hs_col_date')]
            for cx, hdr in zip(col_x, headers):
                ht = self.small_font.render(hdr, True, COLORS['CYAN'])
                s.blit(ht, (cx, content_y))

            sep_y2 = content_y + 28
            pygame.draw.line(s, (60, 60, 150),
                             (int(SCREEN_WIDTH * 0.06), sep_y2),
                             (int(SCREEN_WIDTH * 0.94), sep_y2), 1)

            row_h      = int(SCREEN_HEIGHT * 0.063)
            panel_w    = int(SCREEN_WIDTH  * 0.88)
            panel_x    = int(SCREEN_WIDTH  * 0.06)
            rank_cols  = [COLORS['GOLD'], COLORS['SILVER'], COLORS['BRONZE']]

            for i, sc in enumerate(self.high_score.scores[:10]):
                ry   = sep_y2 + 6 + i * row_h
                rcol = rank_cols[i] if i < 3 else (180, 180, 210)

                row_surf = pygame.Surface((panel_w, row_h - 4), pygame.SRCALPHA)
                row_a    = 80 if i % 2 == 0 else 40
                pygame.draw.rect(row_surf, (30, 30, 70, row_a),
                                 (0, 0, panel_w, row_h - 4), border_radius=6)
                if i < 3:
                    pygame.draw.rect(row_surf, (*rcol, 55),
                                     (0, 0, panel_w, row_h - 4), 1, border_radius=6)
                s.blit(row_surf, (panel_x, ry))

                if i < 3:
                    pygame.draw.circle(s, rcol, (panel_x + 10, ry + (row_h - 4) // 2), 5)

                texts     = [str(i + 1), sc['name'], str(sc['score']), str(sc['level']), sc['date']]
                text_cols = [rcol, rcol, rcol, rcol, (110, 110, 155)]
                for cx, tx, tc in zip(col_x, texts, text_cols):
                    rendered = self.small_font.render(tx, True, tc)
                    s.blit(rendered, rendered.get_rect(midleft=(cx, ry + (row_h - 4) // 2)))

        back = self.font.render(T('back_esc'), True, (90, 90, 150))
        s.blit(back, back.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - int(SCREEN_HEIGHT * 0.05))))

    def draw_how_to_play(self):
        self._draw_themed_bg(T('htp_title'), COLORS['CYAN'])
        s = self.screen

        content_x = int(SCREEN_WIDTH * 0.05)
        content_w = int(SCREEN_WIDTH * 0.90)
        y         = int(SCREEN_HEIGHT * 0.19)
        sec_h     = int(SCREEN_HEIGHT * 0.042)
        line_h    = int(SCREEN_HEIGHT * 0.028)
        empty_h   = int(SCREEN_HEIGHT * 0.010)

        section_colors = {
            T('htp_sec_controls'): (60,  140, 255),
            T('htp_sec_powers'):   (0,   200, 100),
            T('htp_sec_blocks'):   (200, 80,  80),
            T('htp_sec_levels'):   (200, 160, 0),
        }

        for line in self.how_to_play_text:
            if y > SCREEN_HEIGHT - int(SCREEN_HEIGHT * 0.09):
                break
            if line in (T('htp_title'), T('htp_back')):
                continue
            elif line in section_colors:
                sec_col  = section_colors[line]
                sec_surf = pygame.Surface((content_w, sec_h), pygame.SRCALPHA)
                pygame.draw.rect(sec_surf, (*sec_col, 110), (0, 0, content_w, sec_h), border_radius=8)
                pygame.draw.rect(sec_surf, (*sec_col, 190), (0, 0, content_w, sec_h), 1, border_radius=8)
                s.blit(sec_surf, (content_x, y))
                ht = self.font.render(line, True, (255, 255, 255))
                s.blit(ht, (content_x + 14, y + (sec_h - ht.get_height()) // 2))
                y += sec_h + 4
            elif line == "":
                y += empty_h
            else:
                tx = self.small_font.render(line, True, (210, 215, 240))
                s.blit(tx, (content_x + 22, y))
                y += line_h

        back = self.font.render(T('back_esc'), True, (90, 90, 150))
        s.blit(back, back.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - int(SCREEN_HEIGHT * 0.05))))

    def start_game(self):
        self.state = "PLAYING"
        self.current_level = 1
        self.level = Level(self.current_level)
        self.score = 0
        self.lives = 3
        self.game_over = False
        self.level_complete = False
        self.paused = False
        self.waiting_for_launch = True
        self.balls = [Ball(level=self.current_level)]
        self.paddle.reset_size()
        self.paddle.reset_position()
        self.powerups.clear()
        self.active_effects.clear()
        self.particles.clear()
        self.bullets.clear()
        self._fire_timer = 0
        self.barrier.active = False
        self.heart_powerup_count = 0
        self.blocks_destroyed = 0
        self.powerups_collected = 0
        self.start_time = pygame.time.get_ticks()
        self.show_name_input = False
        self.player_name = ""
        self.paddle.color_state = 'normal'
        self.sound.start_music()
    
    def spawn_powerup(self, x, y):
        if random.random() < self.powerup_drop_chance:
            if self.heart_powerup_count >= self.max_heart_powerups:
                power_types = ['B', 'K', 'X', 'O', 'H', 'M', 'Y', 'Z', 'D', 'T', 'A']
            else:
                power_types = ['B', 'K', 'X', 'C', 'O', 'H', 'M', 'Y', 'Z', 'D', 'T', 'A']
            
            power_type = random.choice(power_types)
            
            if power_type == 'C':
                self.heart_powerup_count += 1
            
            self.powerups.append(PowerUp(x, y, power_type))
    
    def create_particles(self, x, y, color):
        for _ in range(10):
            self.particles.append(Particle(x, y, color))
    
    def apply_effect(self, effect_type):
        if effect_type == 'O':
            self.lives -= 1
            self.create_particles(self.paddle.x + self.paddle.width//2, self.paddle.y, COLORS['RED'])
            self.barrier.active = False
            self.barrier.tiles.clear()
            if self.lives <= 0:
                self.game_over = True
                self.sound.play('game_over')
                self._clear_all_effects()
                self.final_score = self.score
                if self.high_score.is_high_score(self.final_score):
                    self.show_name_input = True
            else:
                self.sound.play('life_lost')
        elif effect_type == 'C':
            self.lives += 1
            self.create_particles(self.paddle.x + self.paddle.width//2, self.paddle.y, COLORS['GREEN'])
        elif effect_type == 'B':
            for effect in self.active_effects:
                if effect.type == 'big_paddle':
                    effect.refresh()
                    self.create_particles(self.paddle.x + self.paddle.width//2, self.paddle.y, COLORS['GREEN'])
                    return
            for effect in self.active_effects[:]:
                if effect.type == 'small_paddle':
                    self.active_effects.remove(effect)
            self.paddle.resize(int(PADDLE_WIDTH * 1.5))
            self.paddle.color_state = 'big'
            self.active_effects.append(Effect('big_paddle', 30000))
            self.create_particles(self.paddle.x + self.paddle.width//2, self.paddle.y, COLORS['GREEN'])
        elif effect_type == 'K':
            for effect in self.active_effects:
                if effect.type == 'small_paddle':
                    effect.refresh()
                    self.create_particles(self.paddle.x + self.paddle.width//2, self.paddle.y, COLORS['RED'])
                    return
            for effect in self.active_effects[:]:
                if effect.type == 'big_paddle':
                    self.active_effects.remove(effect)
            self.paddle.resize(int(PADDLE_WIDTH * 0.6))
            self.paddle.color_state = 'small'
            self.active_effects.append(Effect('small_paddle', 30000))
            self.create_particles(self.paddle.x + self.paddle.width//2, self.paddle.y, COLORS['RED'])
        elif effect_type == 'X':
            self._cancel_exclusive_effects('X')
            for effect in self.active_effects:
                if effect.type == 'ghost_ball':
                    effect.refresh()
                    self.create_particles(self.balls[0].x, self.balls[0].y, COLORS['PURPLE'])
                    return
            for ball in self.balls:
                ball.ghost_mode = True
            self.active_effects.append(Effect('ghost_ball', 30000))
            self.create_particles(self.balls[0].x, self.balls[0].y, COLORS['PURPLE'])
        elif effect_type == 'H':
            for effect in self.active_effects:
                if effect.type == 'speed_boost':
                    effect.refresh()
                    self.create_particles(self.balls[0].x, self.balls[0].y, COLORS['YELLOW'])
                    return
            for ball in self.balls:
                ball.set_speed_boost(True)
            self.active_effects.append(Effect('speed_boost', 30000))
            self.create_particles(self.balls[0].x, self.balls[0].y, COLORS['YELLOW'])
        elif effect_type == 'M':
            for effect in self.active_effects:
                if effect.type == 'small_ball':
                    effect.refresh()
                    self.create_particles(self.balls[0].x, self.balls[0].y, COLORS['CYAN'])
                    return
            for ball in self.balls:
                ball.resize(ball.radius * 0.5)
            self.active_effects.append(Effect('small_ball', 30000))
            self.create_particles(self.balls[0].x, self.balls[0].y, COLORS['CYAN'])
        elif effect_type == 'Y':
            self._cancel_exclusive_effects('Y')
            if len(self.balls) < 3:
                src    = self.balls[0]
                to_add = 3 - len(self.balls)
                ref_vy = src.speed_y if src.speed_y != 0 else src.original_speed_y
                for _ in range(to_add):
                    nb = Ball(src.x, src.y, self.current_level, src.radius, src.sticky)
                    nb.speed_x        = src.speed_x * random.choice([-1, 1])
                    nb.speed_y        = ref_vy
                    nb.ghost_mode     = src.ghost_mode
                    nb.speed_boost    = src.speed_boost
                    nb.big_mode       = src.big_mode
                    nb.stuck_to_paddle = src.stuck_to_paddle
                    nb.sticky_cooldown = 75 if nb.sticky else 0
                    self.balls.append(nb)
                self.create_particles(self.balls[0].x, self.balls[0].y, COLORS['PINK'])
        elif effect_type == 'Z':
            self._cancel_exclusive_effects('Z')
            for effect in self.active_effects:
                if effect.type == 'big_ball':
                    effect.refresh()
                    self.create_particles(self.balls[0].x, self.balls[0].y, COLORS['LIME'])
                    return
            for ball in self.balls:
                ball.big_mode = True
                ball.resize(BALL_MAX_RADIUS)
            self.active_effects.append(Effect('big_ball', 30000))
            self.create_particles(self.balls[0].x, self.balls[0].y, COLORS['LIME'])
        elif effect_type == 'D':
            self._cancel_exclusive_effects('D')
            self.barrier.activate(30000)
            self.create_particles(self.paddle.x + self.paddle.width//2, self.paddle.y, COLORS['DARK_BLUE'])
        elif effect_type == 'T':
            self._cancel_exclusive_effects('T')
            for effect in self.active_effects:
                if effect.type == 'sticky_ball':
                    effect.refresh()
                    self.create_particles(self.balls[0].x, self.balls[0].y, COLORS['GOLD'])
                    return
            for ball in self.balls:
                ball.set_sticky(True)
            self.paddle.color_state = 'sticky'
            self.active_effects.append(Effect('sticky_ball', 30000))
            self.create_particles(self.balls[0].x, self.balls[0].y, COLORS['GOLD'])
        elif effect_type == 'A':
            self._cancel_exclusive_effects('A')
            for effect in self.active_effects:
                if effect.type == 'fire_mode':
                    effect.refresh()
                    self.create_particles(self.paddle.x + self.paddle.width//2, self.paddle.y, (255, 80, 0))
                    return
            self.active_effects.append(Effect('fire_mode', 30000))
            self._fire_timer = 0
            self.paddle.color_state = 'fire'
            self.create_particles(self.paddle.x + self.paddle.width//2, self.paddle.y, (255, 80, 0))

    def update_effects(self):
        for effect in self.active_effects[:]:
            if effect.is_expired():
                if effect.type == 'big_paddle':
                    if not any(e.type == 'small_paddle' for e in self.active_effects):
                        self.paddle.reset_size()
                    self.paddle.color_state = 'normal'
                elif effect.type == 'small_paddle':
                    if not any(e.type == 'big_paddle' for e in self.active_effects):
                        self.paddle.reset_size()
                    self.paddle.color_state = 'normal'
                elif effect.type == 'ghost_ball':
                    for ball in self.balls:
                        ball.ghost_mode = False
                        ball.trail_effects.clear()
                elif effect.type == 'speed_boost':
                    for ball in self.balls:
                        ball.set_speed_boost(False)
                elif effect.type == 'small_ball':
                    for ball in self.balls:
                        ball.reset_size()
                elif effect.type == 'big_ball':
                    for ball in self.balls:
                        ball.big_mode = False
                        ball.reset_size()
                elif effect.type == 'sticky_ball':
                    for ball in self.balls:
                        ball.set_sticky(False)
                    self.paddle.color_state = 'normal'
                elif effect.type == 'fire_mode':
                    self.bullets.clear()
                    self._fire_timer = 0
                    if self.paddle.color_state == 'fire':
                        self.paddle.color_state = 'normal'
                self.active_effects.remove(effect)
        
        self.barrier.update()

    def _resume_effects(self):
        if self._effects_paused_at > 0:
            elapsed = pygame.time.get_ticks() - self._effects_paused_at
            for eff in self.active_effects:
                eff.start_time += elapsed
            if self.barrier.active:
                self.barrier.start_time += elapsed
            self._effects_paused_at = 0

    def _clear_all_effects(self):
        self.active_effects.clear()
        self.barrier.active = False
        self.barrier.tiles.clear()
        self.bullets.clear()
        self._fire_timer = 0
        self.paddle.reset_size()
        self.paddle.color_state = 'normal'
        for ball in self.balls:
            ball.ghost_mode = False
            ball.speed_boost = False
            ball.big_mode = False
            ball.set_sticky(False)
            ball.trail_effects.clear()
        self._effects_paused_at = 0

    def _cancel_exclusive_effects(self, picked_type):
        group1 = {'T', 'A', 'Y', 'Z'}
        group2 = {'T', 'X', 'A'}
        to_cancel = set()
        if picked_type in group1:
            to_cancel |= group1
        if picked_type in group2:
            to_cancel |= group2
        to_cancel.discard(picked_type)

        for c in to_cancel:
            if c == 'D':
                self.barrier.active = False
                self.barrier.tiles.clear()
            elif c == 'T':
                for e in self.active_effects[:]:
                    if e.type == 'sticky_ball':
                        self.active_effects.remove(e)
                for ball in self.balls:
                    ball.set_sticky(False)
                if not any(e.type in ('big_paddle', 'small_paddle') for e in self.active_effects):
                    self.paddle.color_state = 'normal'
            elif c == 'A':
                for e in self.active_effects[:]:
                    if e.type == 'fire_mode':
                        self.active_effects.remove(e)
                self.bullets.clear()
                self._fire_timer = 0
                if self.paddle.color_state == 'fire':
                    self.paddle.color_state = 'normal'
            elif c == 'Y':
                if len(self.balls) > 1:
                    self.balls = self.balls[:1]
            elif c == 'Z':
                for e in self.active_effects[:]:
                    if e.type == 'big_ball':
                        self.active_effects.remove(e)
                for ball in self.balls:
                    ball.big_mode = False
                    ball.reset_size()
            elif c == 'X':
                for e in self.active_effects[:]:
                    if e.type == 'ghost_ball':
                        self.active_effects.remove(e)
                for ball in self.balls:
                    ball.ghost_mode = False
                    ball.trail_effects.clear()

    def check_collisions(self):
        for ball in self.balls:
            if not ball.active or ball.stuck_to_paddle:
                continue
                
            closest_x = max(self.paddle.rect.x, min(ball.x, self.paddle.rect.x + self.paddle.rect.width))
            closest_y = max(self.paddle.rect.y, min(ball.y, self.paddle.rect.y + self.paddle.rect.height))
            
            distance = math.sqrt((ball.x - closest_x)**2 + (ball.y - closest_y)**2)
            
            if distance < ball.radius:
                self.sound.play('paddle')
                self.paddle.squish = 8
                if ball.sticky and ball.sticky_cooldown == 0:
                    ball.stuck_to_paddle = True
                    ball.speed_x = 0
                    ball.speed_y = 0
                else:
                    hit_pos = (ball.x - self.paddle.x) / self.paddle.width
                    hit_pos = max(0, min(1, hit_pos))
                    angle = (hit_pos - 0.5) * 1.2
                    
                    speed = math.sqrt(ball.speed_x**2 + ball.speed_y**2)
                    ball.speed_x = speed * math.sin(angle)
                    ball.speed_y = -abs(speed * math.cos(angle))
                
                ball.y = self.paddle.rect.y - ball.radius
    
    def check_block_collisions(self):
        for ball in self.balls:
            if not ball.active or ball.stuck_to_paddle:
                continue

            already_bounced   = False

            for block in self.level.blocks:
                if not block.active:
                    continue

                closest_x = max(block.rect.x, min(ball.x, block.rect.x + block.rect.width))
                closest_y = max(block.rect.y, min(ball.y, block.rect.y + block.rect.height))
                distance  = math.sqrt((ball.x - closest_x)**2 + (ball.y - closest_y)**2)

                if distance >= ball.radius:
                    continue

                # Hayalet top: yön değiştirmez, çoklu bloktan geçer (siyah dahil)
                if ball.ghost_mode:
                    if block.indestructible:
                        block.active = False
                        self.create_particles(block.rect.centerx, block.rect.centery, COLORS['PURPLE'])
                        self.sound.play('block_destroy')
                    else:
                        destroyed = block.hit()
                        if destroyed:
                            self.score += 10 * self.current_level
                            self.blocks_destroyed += 1
                            self.create_particles(block.rect.centerx, block.rect.centery, block.color)
                            self.spawn_powerup(block.rect.centerx, block.rect.centery)
                            self.sound.play('block_destroy')
                    continue  # Hayalet top geçmeye devam eder

                # Çarpma yönü: sadece ilk temas için hesapla
                if not already_bounced:
                    ov_l = abs(ball.x - block.rect.left)
                    ov_r = abs(ball.x - block.rect.right)
                    ov_t = abs(ball.y - block.rect.top)
                    ov_b = abs(ball.y - block.rect.bottom)
                    min_ov = min(ov_l, ov_r, ov_t, ov_b)

                    if min_ov in (ov_l, ov_r):
                        ball.speed_x *= -1
                        ball.x = (block.rect.left - ball.radius) if ball.x < block.rect.centerx \
                                  else (block.rect.right + ball.radius)
                    else:
                        ball.speed_y *= -1
                        ball.y = (block.rect.top - ball.radius) if ball.y < block.rect.centery \
                                  else (block.rect.bottom + ball.radius)
                    ball.rect.x = ball.x - ball.radius
                    ball.rect.y = ball.y - ball.radius
                    already_bounced = True

                if block.indestructible:
                    self.sound.play('wall')
                    break

                # Büyük top: çok vuruşlu bloklar dahil tüm blokları yok eder + alan hasarı
                if ball.big_mode:
                    block.current_hits = block.hits_required
                    block.active       = False
                    destroyed          = True
                    # Impact alanı: en fazla 4 yakın tuğla (toplam max 5)
                    impact_r     = (BLOCK_WIDTH + BLOCK_SPACING) * 1.5
                    impact_count = 0
                    for nearby in self.level.blocks:
                        if impact_count >= 4:
                            break
                        if not nearby.active or nearby.indestructible or nearby is block:
                            continue
                        ndx = nearby.rect.centerx - block.rect.centerx
                        ndy = nearby.rect.centery - block.rect.centery
                        if math.sqrt(ndx * ndx + ndy * ndy) <= impact_r:
                            nearby.current_hits = nearby.hits_required
                            nearby.active = False
                            self.score += 10 * self.current_level
                            self.blocks_destroyed += 1
                            self.create_particles(nearby.rect.centerx, nearby.rect.centery, nearby.color)
                            self.spawn_powerup(nearby.rect.centerx, nearby.rect.centery)
                            impact_count += 1
                else:
                    destroyed = block.hit()

                if destroyed:
                    hits_count = 3 if ball.big_mode else 1
                    self.score += 10 * self.current_level * hits_count
                    self.blocks_destroyed += hits_count
                    self.create_particles(block.rect.centerx, block.rect.centery, block.color)
                    self.spawn_powerup(block.rect.centerx, block.rect.centery)
                    self.sound.play('block_destroy')
                else:
                    self.sound.play('block_hit')
                break
    
    def _fire_bullets(self):
        cannon_r = max(4, self.paddle.height // 2)
        self.bullets.append(Bullet(self.paddle.x + cannon_r, self.paddle.y))
        self.bullets.append(Bullet(self.paddle.x + self.paddle.width - cannon_r, self.paddle.y))

    def check_powerup_collisions(self):
        for powerup in self.powerups[:]:
            dx = powerup.x - self.paddle.x
            dy = powerup.y - self.paddle.y
            closest_x = max(self.paddle.rect.x, min(powerup.x, self.paddle.rect.x + self.paddle.rect.width))
            closest_y = max(self.paddle.rect.y, min(powerup.y, self.paddle.rect.y + self.paddle.rect.height))
            distance = math.sqrt((powerup.x - closest_x)**2 + (powerup.y - closest_y)**2)
            
            if distance < powerup.radius:
                self.apply_effect(powerup.type)
                self.powerups_collected += 1
                if powerup.type != 'O':
                    self.sound.play('powerup')
                self.powerups.remove(powerup)
            elif powerup.y > GAME_AREA_Y + GAME_AREA_HEIGHT:
                self.powerups.remove(powerup)
            else:
                powerup.update()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if self.state == "MENU":
                result = self.menu.update(event)
                if result == "menu_start":
                    self.start_game()
                elif result == "menu_highscores":
                    self.state = "HIGH_SCORES"
                elif result == "menu_howtoplay":
                    self.state = "HOW_TO_PLAY"
                elif result == "menu_settings":
                    self.state = "SETTINGS"
                    self.settings_selected = 0
                elif result == "menu_exit":
                    self.running = False
            
            elif self.state == "HIGH_SCORES":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.state = "MENU"
            
            elif self.state == "HOW_TO_PLAY":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.state = "MENU"

            elif self.state == "SETTINGS":
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_ESCAPE, pygame.K_RETURN):
                        self.settings.save()
                        self.state = "MENU"
                    elif event.key == pygame.K_UP:
                        self.settings_selected = (self.settings_selected - 1) % 4
                    elif event.key == pygame.K_DOWN:
                        self.settings_selected = (self.settings_selected + 1) % 4
                    elif event.key == pygame.K_LEFT:
                        self._settings_adjust(-1)
                    elif event.key == pygame.K_RIGHT:
                        self._settings_adjust(1)
            
            elif self.state == "PLAYING":
                if event.type == pygame.KEYDOWN:
                    if self.show_name_input:
                        if event.key == pygame.K_RETURN and self.player_name:
                            self.high_score.add_score(self.player_name, self.final_score, self.current_level)
                            self.show_name_input = False
                            self.state = "MENU"
                        elif event.key == pygame.K_BACKSPACE:
                            self.player_name = self.player_name[:-1]
                        elif event.key == pygame.K_ESCAPE:
                            self.show_name_input = False
                            self.state = "MENU"
                        elif len(self.player_name) < 15 and event.unicode.isalnum():
                            self.player_name += event.unicode.upper()
                    elif event.key == pygame.K_ESCAPE:
                        self.sound.stop_music()
                        self.state = "MENU"
                        return
                    elif event.key == pygame.K_r and self.game_over:
                        self.start_game()
                    elif event.key == pygame.K_SPACE:
                        if self.waiting_for_launch:
                            self._resume_effects()
                            for ball in self.balls:
                                ball.launch()
                            self.waiting_for_launch = False
                        elif any(b.stuck_to_paddle for b in self.balls):
                            for ball in self.balls:
                                if ball.stuck_to_paddle:
                                    ball.launch()
                        elif any(e.type == 'fire_mode' for e in self.active_effects) and not self.game_over and not self.level_complete and not self.paused:
                            self._fire_bullets()
                        elif not self.game_over and not self.level_complete:
                            self.paused = not self.paused
                    elif event.key == pygame.K_F1:
                        self.show_help = not self.show_help
                    elif event.key == pygame.K_m:
                        self.mouse_control = not self.mouse_control
                
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.waiting_for_launch:
                        self._resume_effects()
                        for ball in self.balls:
                            ball.launch()
                        self.waiting_for_launch = False
                    elif any(b.stuck_to_paddle for b in self.balls):
                        for ball in self.balls:
                            if ball.stuck_to_paddle:
                                ball.launch()
                    elif any(e.type == 'fire_mode' for e in self.active_effects) and not self.game_over and not self.level_complete and not self.paused:
                        self._fire_bullets()
                
                elif event.type == pygame.MOUSEMOTION and self.mouse_control and not self.game_over and not self.paused:
                    self.mouse_x = event.pos[0]
    
    def update(self):
        if self.paused or self.game_over:
            return

        if not self.waiting_for_launch:
            self.update_effects()
        self.particles = [p for p in self.particles if p.update()]
        
        if self.mouse_control:
            self.paddle.update(self.mouse_x)
        else:
            self.paddle.update()
        
        for ball in self.balls:
            ball.update(self.paddle.rect if (self.waiting_for_launch or ball.stuck_to_paddle) else None)
        
        self.check_powerup_collisions()
        
        lost_balls = []
        for ball in self.balls:
            if ball.stuck_to_paddle or not ball.active:
                continue
            bounced = False
            if self.barrier.active and self.barrier.tiles and ball.speed_y > 0:
                barrier_top = self.barrier.tiles[0].y
                if ball.y + ball.radius >= barrier_top:
                    ball.rect.x = int(ball.x - ball.radius)
                    ball.rect.y = int(ball.y - ball.radius)
                    if self.barrier.check_collision(ball):
                        ball.y = barrier_top - ball.radius
                        ball.rect.y = int(ball.y - ball.radius)
                        ball.speed_y = -abs(ball.speed_y)
                        self.create_particles(int(ball.x), int(barrier_top), COLORS['CYAN'])
                        bounced = True
            if not bounced and ball.y + ball.radius > GAME_AREA_Y + GAME_AREA_HEIGHT:
                lost_balls.append(ball)
        
        for ball in lost_balls:
            self.balls.remove(ball)
            self.create_particles(ball.x, ball.y, COLORS['RED'])
        
        if len(self.balls) == 0 and lost_balls:
            self.lives -= 1
            if self.lives > 0:
                self._clear_all_effects()
                self.balls = [Ball(level=self.current_level)]
                self.waiting_for_launch = True
                self.sound.play('life_lost')
            else:
                self.game_over = True
                self.sound.play('game_over')
                self._clear_all_effects()
                self.final_score = self.score
                if self.high_score.is_high_score(self.final_score):
                    self.show_name_input = True

        if any(b.wall_hit for b in self.balls if b.active and not b.stuck_to_paddle):
            self.sound.play('wall')

        # Büyük top duvar patlaması: yandaki bloklara şok dalgası
        for ball in self.balls:
            if ball.big_mode and ball.wall_hit and ball.active and not ball.stuck_to_paddle:
                splash_r = BALL_MAX_RADIUS * 7
                splash_count = 0
                for block in self.level.blocks:
                    if not block.active or block.indestructible:
                        continue
                    dx = block.rect.centerx - ball.x
                    dy = block.rect.centery - ball.y
                    if math.sqrt(dx * dx + dy * dy) <= splash_r:
                        block.current_hits = block.hits_required
                        block.active = False
                        self.score += 10 * self.current_level * 2
                        self.blocks_destroyed += 2
                        self.create_particles(block.rect.centerx, block.rect.centery, block.color)
                        splash_count += 1
                        if splash_count >= 4:
                            break

        self.check_collisions()
        self.check_block_collisions()

        # Mermi güncelle + blok çarpışması
        for bullet in self.bullets[:]:
            if not bullet.update():
                self.bullets.remove(bullet)
                continue
            for block in self.level.blocks:
                if not block.active:
                    continue
                br = pygame.Rect(int(bullet.x - bullet.radius), int(bullet.y - bullet.radius),
                                  bullet.radius * 2, bullet.radius * 2)
                if block.rect.colliderect(br):
                    if not block.indestructible:
                        block.current_hits = block.hits_required
                        block.active = False
                        self.score += 10 * self.current_level
                        self.blocks_destroyed += 1
                        self.create_particles(block.rect.centerx, block.rect.centery, block.color)
                        self.spawn_powerup(block.rect.centerx, block.rect.centery)
                        self.sound.play('block_destroy')
                    self.bullets.remove(bullet)
                    break

        if self.level.all_blocks_destroyed() and not self.level_complete:
            self.level_complete = True
            self.create_particles(GAME_AREA_X + GAME_AREA_WIDTH//2, GAME_AREA_Y + GAME_AREA_HEIGHT//2, COLORS['GOLD'])

            if self.current_level >= 10:
                self.game_over = True
                self.sound.play('game_over')
                self._clear_all_effects()
                self.final_score = self.score
                if self.high_score.is_high_score(self.final_score):
                    self.show_name_input = True
            else:
                self.sound.play('level_complete')
                self.next_level()
    
    def next_level(self):
        self.current_level += 1
        if self.current_level <= 10:
            self.level = Level(self.current_level)
            self.level_complete = False
            self.waiting_for_launch = True
            self.powerups.clear()
            self._clear_all_effects()
            self.balls = [Ball(level=self.current_level)]
            self.paddle.reset_position()
    
    def draw_text(self):
        # TÜM BİLGİLER İÇİN AYNI FONT - self.font kullan
        info_y = GAME_AREA_Y + 20
        
        score_text = self.font.render(f"{T('hud_score')}: {self.score}", True, COLORS['WHITE'])
        lives_text = self.font.render(f"{T('hud_lives')}: {self.lives}", True, COLORS['WHITE'])
        level_text = self.font.render(f"{T('hud_level')}: {self.current_level}/10", True, COLORS['YELLOW'])
        
        # Metinlerin yüksekliklerini al (hepsi aynı fonttan dolayı aynı olacak)
        text_height = score_text.get_height()
        
        score_rect = score_text.get_rect(midleft=(GAME_AREA_X + 20, info_y))
        lives_rect = lives_text.get_rect(midright=(GAME_AREA_X + GAME_AREA_WIDTH - 20, info_y))
        level_rect = level_text.get_rect(center=(GAME_AREA_X + GAME_AREA_WIDTH // 2, info_y))
        
        self.screen.blit(score_text, score_rect)
        self.screen.blit(lives_text, lives_rect)
        self.screen.blit(level_text, level_rect)
        
        # Aktif efektler: skor satırının hemen altında yatay rozet şeridi
        _badge_map = {
            'big_paddle':   (COLORS['GREEN'],  T('badge_big_paddle')),
            'small_paddle': (COLORS['RED'],    T('badge_small_paddle')),
            'ghost_ball':   (COLORS['PURPLE'], T('badge_ghost')),
            'speed_boost':  (COLORS['YELLOW'], T('badge_speed')),
            'small_ball':   (COLORS['CYAN'],   T('badge_small_ball')),
            'big_ball':     (COLORS['LIME'],   T('badge_big_ball')),
            'sticky_ball':  (COLORS['GOLD'],   T('badge_sticky')),
            'fire_mode':    ((220, 80, 0),     T('badge_fire')),
        }
        badge_h  = text_height - 8
        badge_y  = info_y + text_height // 2 + 4
        badge_x  = GAME_AREA_X + 20
        br_badge = badge_h // 2

        display_now = self._effects_paused_at if self._effects_paused_at > 0 else pygame.time.get_ticks()

        for effect in self.active_effects:
            if effect.type not in _badge_map:
                continue
            col, lbl = _badge_map[effect.type]
            label = f"{lbl}:{effect.get_remaining(display_now)}s"
            tw  = self.tiny_font.size(label)[0]
            bw  = tw + 12
            bs  = pygame.Surface((bw, badge_h), pygame.SRCALPHA)
            pygame.draw.rect(bs, (*col, 160), (0, 0, bw, badge_h), border_radius=br_badge)
            pygame.draw.rect(bs, (*col, 240), (0, 0, bw, badge_h), 1, border_radius=br_badge)
            self.screen.blit(bs, (badge_x, badge_y))
            ts = self.tiny_font.render(label, True, (255, 255, 255))
            self.screen.blit(ts, ts.get_rect(center=(badge_x + bw // 2, badge_y + badge_h // 2)))
            badge_x += bw + 5

        if self.barrier.active:
            remaining = max(0, (self.barrier.duration - (display_now - self.barrier.start_time)) // 1000)
            col   = (180, 120, 60)
            label = f"{T('badge_barrier')}:{remaining}s"
            tw    = self.tiny_font.size(label)[0]
            bw    = tw + 12
            bs    = pygame.Surface((bw, badge_h), pygame.SRCALPHA)
            pygame.draw.rect(bs, (*col, 160), (0, 0, bw, badge_h), border_radius=br_badge)
            pygame.draw.rect(bs, (*col, 240), (0, 0, bw, badge_h), 1, border_radius=br_badge)
            self.screen.blit(bs, (badge_x, badge_y))
            ts = self.tiny_font.render(label, True, (255, 255, 255))
            self.screen.blit(ts, ts.get_rect(center=(badge_x + bw // 2, badge_y + badge_h // 2)))
    
        if self.waiting_for_launch and not self.game_over and not self.level_complete:
            wait_text = self.title_font.render(T('ready'), True, COLORS['YELLOW'])
            wait_rect = wait_text.get_rect(center=(GAME_AREA_X + GAME_AREA_WIDTH//2, GAME_AREA_Y + GAME_AREA_HEIGHT//2 - 50))
            self.screen.blit(wait_text, wait_rect)
            space_text = self.font.render(T('launch_hint'), True, COLORS['GREEN'])
            space_rect = space_text.get_rect(center=(GAME_AREA_X + GAME_AREA_WIDTH//2, GAME_AREA_Y + GAME_AREA_HEIGHT//2 + 20))
            self.screen.blit(space_text, space_rect)
        elif any(b.stuck_to_paddle for b in self.balls) and not self.game_over and not self.level_complete:
            hint = self.small_font.render(T('launch_hint2'), True, COLORS['GOLD'])
            self.screen.blit(hint, hint.get_rect(center=(GAME_AREA_X + GAME_AREA_WIDTH//2,
                                                          self.paddle.y - 35)))
        elif any(e.type == 'fire_mode' for e in self.active_effects) and not self.game_over and not self.level_complete and not self.waiting_for_launch:
            hint = self.small_font.render(T('fire_hint'), True, (255, 120, 0))
            self.screen.blit(hint, hint.get_rect(center=(GAME_AREA_X + GAME_AREA_WIDTH//2,
                                                          self.paddle.y - 35)))
        
        if self.paused and not self.game_over and not self.level_complete and not self.waiting_for_launch:
            pause_text = self.title_font.render(T('paused'), True, COLORS['YELLOW'])
            pause_rect = pause_text.get_rect(center=(GAME_AREA_X + GAME_AREA_WIDTH//2, GAME_AREA_Y + GAME_AREA_HEIGHT//2))
            self.screen.blit(pause_text, pause_rect)
            pause_inst = self.small_font.render(T('pause_hint'), True, COLORS['WHITE'])
            pause_inst_rect = pause_inst.get_rect(center=(GAME_AREA_X + GAME_AREA_WIDTH//2, GAME_AREA_Y + GAME_AREA_HEIGHT//2 + 60))
            self.screen.blit(pause_inst, pause_inst_rect)
        
        if self.game_over and not self.show_name_input:
            rank      = self.high_score.get_rank(self.score)
            completed = self.level_complete and self.current_level >= 10

            if completed:
                game_text  = self.title_font.render(T('completed'), True, COLORS['GOLD'])
                score_text = self.font.render(f"{T('total_score')}: {self.score}", True, COLORS['WHITE'])
            else:
                game_text  = self.title_font.render(T('game_over_text'), True, COLORS['RED'])
                score_text = self.font.render(f"{T('score_label')}: {self.score}  ({T('level_label')} {self.current_level})", True, COLORS['WHITE'])

            stats_text = self.small_font.render(
                f"{T('blocks_destroyed')}: {self.blocks_destroyed} | {T('powers_collected')}: {self.powerups_collected}",
                True, COLORS['SILVER'])

            if rank <= 10:
                rank_text = self.small_font.render(f"{T('rank_label')}: {rank}{T('rank_suffix')}", True, COLORS['GREEN'])
            else:
                rank_text = self.small_font.render(f"{T('rank_label')}: {T('rank_outside')}", True, COLORS['YELLOW'])

            restart_text = self.font.render(T('restart_hint'), True, COLORS['GREEN'])
            menu_text    = self.font.render(T('menu_esc'), True, COLORS['YELLOW'])

            cx = GAME_AREA_X + GAME_AREA_WIDTH // 2
            cy = GAME_AREA_Y + GAME_AREA_HEIGHT // 2
            self.screen.blit(game_text,    game_text.get_rect(center=(cx, cy - 100)))
            self.screen.blit(score_text,   score_text.get_rect(center=(cx, cy - 40)))
            self.screen.blit(stats_text,   stats_text.get_rect(center=(cx, cy)))
            self.screen.blit(rank_text,    rank_text.get_rect(center=(cx, cy + 40)))
            self.screen.blit(restart_text, restart_text.get_rect(center=(cx, cy + 100)))
            self.screen.blit(menu_text,    menu_text.get_rect(center=(cx, cy + 140)))
    
    def draw_name_input(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(COLORS['BLACK'])
        self.screen.blit(overlay, (0, 0))
        
        title_text = self.title_font.render(T('new_record'), True, COLORS['GOLD'])
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 100))
        self.screen.blit(title_text, title_rect)

        score_text = self.font.render(f"{T('your_score')}: {self.final_score}", True, COLORS['WHITE'])
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 40))
        self.screen.blit(score_text, score_rect)

        rank = self.high_score.get_rank(self.final_score)
        rank_text = self.font.render(f"{T('rank_label')}: {rank}{T('rank_suffix')}", True, COLORS['GREEN'])
        rank_rect = rank_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        self.screen.blit(rank_text, rank_rect)

        name_text = self.font.render(T('enter_name'), True, COLORS['WHITE'])
        name_rect = name_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 60))
        self.screen.blit(name_text, name_rect)
        
        input_box = pygame.Rect(SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2 + 110, 300, 50)
        pygame.draw.rect(self.screen, COLORS['WHITE'], input_box, 2)
        
        display_name = self.player_name
        if pygame.time.get_ticks() % 1000 < 500:
            display_name += "_"
        
        name_surface = self.font.render(display_name, True, COLORS['WHITE'])
        name_rect = name_surface.get_rect(center=input_box.center)
        self.screen.blit(name_surface, name_rect)
        
        inst_text = self.small_font.render(T('save_hint'), True, COLORS['GREEN'])
        inst_rect = inst_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 190))
        self.screen.blit(inst_text, inst_rect)
    
    def run(self):
        while self.running:
            self.handle_events()
            
            if self.state == "MENU":
                self.menu.draw()
            elif self.state == "HIGH_SCORES":
                self.draw_high_scores_screen()
            elif self.state == "HOW_TO_PLAY":
                self.draw_how_to_play()
            elif self.state == "SETTINGS":
                self.draw_settings_screen()
            elif self.state == "PLAYING":
                if not self.game_over and not self.paused:
                    self.update()
                
                self.level.draw(self.screen)
                
                for powerup in self.powerups:
                    powerup.draw(self.screen)
                
                for particle in self.particles:
                    particle.draw(self.screen)

                for bullet in self.bullets:
                    bullet.draw(self.screen)

                self.paddle.draw(self.screen)
                self.barrier.draw(self.screen)
                
                for ball in self.balls:
                    ball.draw(self.screen)
                
                self.draw_text()
                
                if self.show_name_input:
                    self.draw_name_input()
            
            draw_frame(self.screen)
            
            pygame.display.flip()
            self.clock.tick(self.settings.fps)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()