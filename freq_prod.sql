WITH tb_freq_abs AS(

 SELECT descProduto, count(idTransacao) AS FreqAbs

FROM points

GROUP BY descProduto

),

tb_freq_abs_cum AS(

SELECT *,
sum(FreqABS) OVER (ORDER BY descProduto) AS FreqAbsAcum,
FreqAbs / (SELECT sum (FreqAbs) FROM tb_freq_abs)

FROM tb_freq_abs
)

SELECT * FROM tb_freq_abs_cum