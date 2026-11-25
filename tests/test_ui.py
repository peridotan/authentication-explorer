from playwright.sync_api import sync_playwright
from pathlib import Path
s=(Path(__file__).resolve().parents[1]/'index.html').read_text()
with sync_playwright() as p:
 b=p.chromium.launch(args=['--no-sandbox']);pg=b.new_page(viewport={'width':1440,'height':800});err=[];pg.on('pageerror',lambda e:err.append(str(e)));pg.set_content(s);pg.wait_for_timeout(100)
 pg.locator('[data-mode=attack]').click();assert pg.locator('#comparison').is_visible() and not pg.locator('#sim').is_visible();assert pg.locator('[data-mode]').count()==2
 assert pg.locator('[data-compare]').count()==17;assert pg.locator('#matrix td span.neutral').count()==8
 pairs=pg.locator('[data-compare]').evaluate_all('(es)=>es.map(e=>[e.dataset.compare,e.className])')
 for pair,tone in pairs:
  pg.locator(f'[data-compare="{pair}"]').click();assert pg.locator('#sim').is_visible() and not pg.locator('#comparison').is_visible();assert pg.locator('#progress').inner_text().startswith('STEP 1 /');assert pg.evaluate('()=>[STATE.scenario,STATE.method].join(":")')==pair
  pg.locator('#timeline button').last.click();assert tone in pg.locator('#result').get_attribute('class').split();pg.locator('#backMatrix').click();assert pg.locator('#comparison').is_visible() and not pg.locator('#sim').is_visible()
 for m in ['normal']:
  pg.locator(f'[data-mode={m}]').click();assert pg.locator('#sim').is_visible() and not pg.locator('#comparison').is_visible()
 print('17 matrix round trips; 8 unavailable; other modes OK; errors',err)
 for w,h in [(1440,800),(1280,720),(1366,768),(1920,1080)]:
  pg.set_viewport_size({'width':w,'height':h});pg.locator('[data-mode=normal]').click();pg.wait_for_timeout(100)
  coords=lambda:pg.evaluate('()=>[...document.querySelectorAll(\'[data-node="browser"] rect.node,[data-node="app"] rect.node,[data-node="auth"] rect.node,[data-node="server"] rect.node\')].map(e=>{let r=e.getBoundingClientRect();return [r.x,r.y,r.width,r.height]})')
  for f in range(3):
   pg.locator('[data-mode=normal]').click();pg.wait_for_timeout(70);base=coords();pg.locator('[data-mode=attack]').click();pg.locator('[data-compare="phish:pk"]').click();pg.wait_for_timeout(100);after=coords();bot=pg.locator('.workspace>.main').bounding_box();print(w,h,f,base==after,'bottom',round(bot['y']+bot['height'],1));assert base==after and bot['y']+bot['height']<=h;pg.locator('#font').click();pg.wait_for_timeout(70)
 assert not err
 b.close()
