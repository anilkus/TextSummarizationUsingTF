![image](https://github.com/anilkus/TextSummarizationUsingTF/assets/16832969/098d44b2-d961-4f45-9082-34df6cb455b4)

# TextSummarizationUsingTF
Text summarization using only term frequency (TF) is a simple and basic approach that relies on counting the occurrences of each word in a document (input text) and using those counts to create a summary. The TF method does not consider the context or semantics of the words; it only considers their frequency of occurrence in the document.

Here's a basic outline of how you can implement a TF-based text summarization approach:

Data Preprocessing: Tokenize the input text into words (or subwords) and convert them to lowercase. Remove any punctuation or special characters, and filter out common stop words (e.g., "the," "is," "and," etc.), as they are unlikely to contribute significantly to the summary.

Term Frequency Calculation: Calculate the term frequency (TF) of each word in the document. TF is simply the number of times a word appears in the document divided by the total number of words in the document.

Selecting Important Words: Rank the words based on their TF scores, and select the top N words with the highest TF scores. These words will form the summary.

Reconstructing the Summary: Reconstruct the summary by joining the selected words to form coherent sentences or phrases. You may use additional heuristics or rules to ensure the summary is grammatically correct.

Keep in mind that this basic TF-based summarization approach has limitations:

It does not consider the relationships between words or the semantic meaning of the text, leading to potentially shallow and less informative summaries.
The summary length is fixed and may not be suitable for different documents with varying content lengths.
It may not capture the most important or relevant information in the document, as the importance of a word is solely based on its frequency.
Despite its simplicity, this approach can be a good starting point for simple summarization tasks or as a baseline for more advanced methods. More sophisticated approaches, such as using machine learning or deep learning models, like those mentioned in previous responses, are likely to produce more accurate and informative summaries for complex texts.

How to save all we have done in Excel ? 
We are performing automatic Excel filling operations using Python to record the characteristics and success metrics of the summaries generated here. For this purpose, we have created a table in Excel, and we are populating the relevant cells using Python. Please review the excel.py file for this process.

--------------------------------------------------------------------------------------------------------------

Sadece terim sıklığı (TF) kullanarak metin özeti, her kelimenin bir belgede (giriş metni) kaç kez geçtiğini sayarak ve bu sayıları kullanarak bir özet oluşturan basit ve temel bir yaklaşımdır. TF yöntemi, kelimelerin bağlamını veya anlamını dikkate almaz; yalnızca belgedeki geçme sıklıklarını düşünür.

İşte TF tabanlı metin özetleme yaklaşımını nasıl uygulayabileceğinizin temel çizgisi:

Veri Ön İşleme: Giriş metnini kelimelere (veya alt kelimelere) böler ve küçük harflere dönüştürür. Noktalama işaretlerini veya özel karakterleri kaldırır ve yaygın olan durdurma kelimelerini ("ve", "ise", "ve" gibi) filtreler, çünkü bu kelimeler özete önemli ölçüde katkıda bulunmazlar.

Terim Sıklığı Hesaplama: Belgedeki her kelimenin terim sıklığını (TF) hesaplar. TF, bir kelimenin belgede kaç kez geçtiğinin belgedeki toplam kelime sayısına bölünmesiyle elde edilir.

Önemli Kelimelerin Seçimi: Kelimeleri TF puanlarına göre sıralar ve en yüksek TF puanına sahip ilk N kelimeyi seçer. Bu kelimeler özeti oluşturacaktır.

Özeti Yeniden Oluşturma: Seçilen kelimeleri birleştirerek özeti anlamlı cümleler veya ifadeler halinde yeniden oluşturur. Özetin dilbilgisel olarak doğru olmasını sağlamak için ek heuristikler veya kurallar kullanabilirsiniz.

Bu temel TF tabanlı özetleme yaklaşımının bazı sınırlamaları olduğunu unutmayın:

Kelimeler arasındaki ilişkileri veya metnin anlamını dikkate almaz, bu da yüzeysel ve daha az bilgilendirici özetlere yol açabilir.

Özet uzunluğu sabittir ve farklı içerik uzunluklarına sahip belgeler için uygun olmayabilir.
Belgenin en önemli veya ilgili bilgilerini yakalayamayabilir, çünkü bir kelimenin önemi yalnızca sıklığına dayalıdır.
Bu basit yaklaşım, temel özetleme görevleri için iyi bir başlangıç noktası veya karmaşık metinler için daha doğru ve bilgilendirici özetler üretmek için daha gelişmiş yöntemlerin temeli olarak kullanılabilir. Önceki yanıtlarda bahsedilen makine öğrenimi veya derin öğrenme modellerini kullanan daha sofistike yaklaşımlar, daha karmaşık metinler için daha iyi sonuçlar üretme eğilimindedir.

Excel'e özetlemelerin sonuçlarını nasıl aktarabiliriz? 
Burada ürettiğimiz özetlerin özelliklkerini ve başarı metriklerini kaydetmek için python ile otomatik excel doldurma işlemleri yapıyoruz bunun için excelde bir tablo oluşturup ilgili boşukları python üzerinden dolduruyoruz lütfen bunun için excel.py dosyasını inceleyiniz.
