# h t t p s : / / m a c h i n e l e a r n i n g m a s t e r y . c o m / m a c h i n e - l e a r n i n g - i n - p y t h o n - s t e p - b y - s t e p / 
 
 #   L o a d   l i b r a r i e s 
 i m p o r t   p a n d a s 
 f r o m   p a n d a s . t o o l s . p l o t t i n g   i m p o r t   s c a t t e r _ m a t r i x 
 i m p o r t   m a t p l o t l i b . p y p l o t   a s   p l t 
 f r o m   s k l e a r n   i m p o r t   m o d e l _ s e l e c t i o n 
 f r o m   s k l e a r n . m e t r i c s   i m p o r t   c l a s s i f i c a t i o n _ r e p o r t 
 f r o m   s k l e a r n . m e t r i c s   i m p o r t   c o n f u s i o n _ m a t r i x 
 f r o m   s k l e a r n . m e t r i c s   i m p o r t   a c c u r a c y _ s c o r e 
 f r o m   s k l e a r n . m e t r i c s   i m p o r t   * 
 f r o m   s k l e a r n . l i n e a r _ m o d e l   i m p o r t   L o g i s t i c R e g r e s s i o n 
 f r o m   s k l e a r n . t r e e   i m p o r t   D e c i s i o n T r e e C l a s s i f i e r 
 f r o m   s k l e a r n . n e i g h b o r s   i m p o r t   K N e i g h b o r s C l a s s i f i e r 
 f r o m   s k l e a r n . d i s c r i m i n a n t _ a n a l y s i s   i m p o r t   L i n e a r D i s c r i m i n a n t A n a l y s i s 
 f r o m   s k l e a r n . n a i v e _ b a y e s   i m p o r t   G a u s s i a n N B 
 f r o m   s k l e a r n . s v m   i m p o r t   S V C 
 
 u r l   =   " h t t p s : / / a r c h i v e . i c s . u c i . e d u / m l / m a c h i n e - l e a r n i n g - d a t a b a s e s / i r i s / i r i s . d a t a " 
 n a m e s   =   [ ' s e p a l - l e n g t h ' , ' s e p a l - w i d t h ' , ' p e t a l - l e n g t h ' , ' p e t a l - w i d t h ' ,   ' c l a s s ' ] 
 d a t a s e t   =   p a n d a s . r e a d _ c s v ( u r l ,   n a m e s = n a m e s ) 
 
 # p r i n t ( d a t a s e t . s h a p e ) 
 
 # p r i n t ( d a t a s e t . h e a d ( 2 0 ) ) 
 # p r i n t ( d a t a s e t . d e s c r i b e ( ) ) 
 
 # " A   r e a l l y   i m p o r t a n t   t h i n g   t o   k n o w   i s   t h a t   s c i k i t - l e a r n   e s t i m a t o r s   * * o n l y   t a k e   i n   c o n t i n u o u s   d a t a   i n   t h e   f o r m   o f   N u m P y   a r r a y s * * .   I f   y o u r   d a t a   i s   a l r e a d y   c o n t i n u o u s ,   t h i s   i s n ' t   a   p r o b l e m .   T h e r e ' s   a   f u n c t i o n   i n   N u m P y   c a l l e d   l o a d t x t ( )   t h a t   c a n   r e a d   i n   a   C S V   f i l e   a n d   c o n v e r t   i t   t o   a n   a r r a y   w i t h   e a s e .   F o r   e x a m p l e ,   h e r e ' s   b o t h   t h e   f i r s t   f i v e   d a t a   i n s t a n c e s   a n d   t h e i r   l a b e l s   f r o m   t h e   g l a s s   i d e n t i f i c a t i o n   d a t a s e t . " 
 p r i n t   " H i " 
 
 #   S p l i t - o u t   v a l i d a t i o n   d a t a s e t 
 a r r a y   =   d a t a s e t . v a l u e s 
 X   =   a r r a y [ : , 0 : 4 ] 
 Y   =   a r r a y [ : , 4 ] 
 v a l i d a t i o n _ s i z e   =   0 . 3 0 
 s e e d   =   7 
 X _ t r a i n ,   X _ v a l i d a t i o n ,   Y _ t r a i n ,   Y _ v a l i d a t i o n   =   m o d e l _ s e l e c t i o n . t r a i n _ t e s t _ s p l i t ( X ,   Y ,   t e s t _ s i z e = v a l i d a t i o n _ s i z e ,   r a n d o m _ s t a t e = s e e d ) 
 
 s c o r i n g   =   ' a c c u r a c y ' 
 
 
 #   M a k e   p r e d i c t i o n s   o n   v a l i d a t i o n   d a t a s e t 
 k n n   =   K N e i g h b o r s C l a s s i f i e r ( ) 
 k n n . f i t ( X _ t r a i n ,   Y _ t r a i n ) 
 p r e d i c t i o n s   =   k n n . p r e d i c t ( X _ v a l i d a t i o n ) 
 p r i n t ( a c c u r a c y _ s c o r e ( Y _ v a l i d a t i o n ,   p r e d i c t i o n s ) ) 
 p r i n t ( c o n f u s i o n _ m a t r i x ( Y _ v a l i d a t i o n ,   p r e d i c t i o n s ) ) 
 p r i n t ( c l a s s i f i c a t i o n _ r e p o r t ( Y _ v a l i d a t i o n ,   p r e d i c t i o n s ) ) 
 p r i n t ( c o h e n _ k a p p a _ s c o r e ( Y _ v a l i d a t i o n , p r e d i c t i o n s ) ) 
 
 
 
 s v m   =   S V C ( ) 
 s v m . f i t ( X _ t r a i n , Y _ t r a i n ) 
 p r e d i c t i o n s   =   s v m . p r e d i c t ( X _ v a l i d a t i o n ) 
 p r i n t ( a c c u r a c y _ s c o r e ( Y _ v a l i d a t i o n ,   p r e d i c t i o n s ) ) 
 p r i n t ( c o n f u s i o n _ m a t r i x ( Y _ v a l i d a t i o n ,   p r e d i c t i o n s ) ) 
 p r i n t ( c l a s s i f i c a t i o n _ r e p o r t ( Y _ v a l i d a t i o n ,   p r e d i c t i o n s ) ) 
 