WITH tb_freq_abs AS(

 SELECT qtdPontos, count(idTransacao) AS FreqAbs

FROM points

GROUP BY qtdPontos

),

tb_freq_abs_cum AS(

SELECT *,
sum(FreqABS) OVER (ORDER BY qtdPontos) AS FreqAbsAcum,
1.0 * FreqAbs / (SELECT sum (FreqAbs) FROM tb_freq_abs) AS FreqRelativa

FROM tb_freq_abs
)

SELECT *,
sum(FreqRelativa) OVER (ORDER BY qtdPontos) as FreqRelativa
  FROM tb_freq_abs_cum