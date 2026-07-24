<!--  File:  TEST - Literature_Review_DT_SVM_KNN_Diabetes.md  -->
<!--  Model:  local-model  -->
<!--  DPI:  120  -->

<!--  Page 1  -->

JURNAL PENGANTAR KECERDASAN BUATAN,
VOL. 1 NO 1, April 2026, 1-11

Literature Review Perbandingan Algoritma Decision Tree, Support Vector Machine, dan K-Nearest Neighbor dalam Klasifikasi Prediksi Diabetes

Teuku Edwin Pratama ¹), Deo Saputra ²), Rizqi Al Fajri ³)

¹) Universitas Indo Global Mandiri
Email : 2024210016@students.uigm.ac.id ¹)

ABSTRAK

Diabetes mellitus merupakan salah satu penyakit kronis yang memiliki tingkat prevalensi tinggi secara global dan menjadi penyebab utama berbagai komplikasi serius seperti penyakit jantung, gagal ginjal, dan gangguan saraf. Penyakit ini ditandai dengan tingginya kadar glukosa dalam darah akibat gangguan produksi atau fungsi insulin. Berdasarkan berbagai penelitian, jumlah penderita diabetes terus meningkat setiap tahunnya sehingga diperlukan metode deteksi dini yang akurat dan efisien untuk membantu proses diagnosis (Kowsher et al., 2019). Perkembangan teknologi, khususnya dalam bidang machine learning, telah memberikan solusi dalam mendukung diagnosis penyakit secara otomatis. Machine learning mampu menganalisis data medis dalam jumlah besar serta menemukan pola yang tidak terlihat secara langsung oleh manusia. Dalam konteks prediksi diabetes, algoritma klasifikasi seperti Decision Tree (DT), Support Vector Machine (SVM), dan K-Nearest Neighbor (KNN) menjadi metode yang paling banyak digunakan dalam berbagai penelitian (Arsyad et al., 2024). Penelitian ini bertujuan untuk melakukan literature review terhadap perbandingan performa algoritma Decision Tree, Support Vector Machine, dan K-Nearest Neighbor dalam klasifikasi prediksi diabetes. Metode yang digunakan adalah studi literatur dengan menganalisis berbagai jurnal ilmiah yang relevan, baik nasional maupun internasional. Parameter evaluasi yang digunakan dalam penelitian meliputi accuracy, precision, recall, dan F1-score sebagai indikator utama performa model. Hasil kajian menunjukkan bahwa algoritma Support Vector Machine (SVM) secara umum memiliki performa terbaik dalam hal akurasi, dengan nilai mencapai 94,5% dibandingkan dengan KNN sebesar 92,5% dan Decision Tree sebesar 93,5% (Saleh et al., 2025). Selain itu, penelitian lain juga menunjukkan bahwa SVM dapat mencapai akurasi hingga 100% dalam kondisi tertentu (Ardiansyah et al., 2024). Di sisi lain, Decision Tree menunjukkan keunggulan dalam hal interpretasi model dan stabilitas performa, terutama setelah dilakukan optimasi parameter menggunakan teknik seperti GridSearchCV yang mampu meningkatkan akurasi hingga 97,06% (Pratama, 2024). Sementara itu, K-Nearest Neighbor memiliki keunggulan dalam kesederhanaan implementasi, namun memiliki keterbatasan dalam menangani dataset berukuran besar serta sensitif terhadap noise (Yunianto & Subhiyakto, 2025). Dengan demikian, dapat disimpulkan bahwa tidak terdapat satu algoritma yang secara mutlak unggul dalam semua kondisi. Pemilihan algoritma terbaik harus disesuaikan dengan karakteristik data serta kebutuhan sistem yang akan dikembangkan.

Kata Kunci : Diabetes Mellitus, Machine Learning, Decision Tree, Support Vector Machine, K-Nearest Neighbor.

<!-- End of 1 -->

<!--  Page 2  -->

JURNAL PENGANTAR KECERDASAN BUATAN,
VOL. 1 NO 1, April 2026, 1-11

1. PENDAHULUAN

Diabetes mellitus merupakan salah satu penyakit metabolik kronis yang menjadi permasalahan serius dalam bidang kesehatan global. Penyakit ini ditandai dengan meningkatnya kadar glukosa dalam darah akibat gangguan produksi insulin atau ketidakmampuan tubuh dalam menggunakan insulin secara efektif. Jika tidak ditangani dengan baik, diabetes dapat menyebabkan berbagai komplikasi serius seperti penyakit jantung, gagal ginjal, kerusakan saraf, hingga kebutaan (Kowsher et al., 2019).

Berdasarkan laporan berbagai penelitian, jumlah penderita diabetes terus meningkat secara signifikan dari tahun ke tahun. Kondisi ini menjadikan diabetes sebagai salah satu penyakit dengan tingkat prevalensi tertinggi di dunia. Selain itu, banyak penderita diabetes yang tidak menyadari kondisi mereka pada tahap awal, sehingga deteksi dini menjadi sangat penting untuk mencegah komplikasi yang lebih berisiko (Vaishnavi et al., 2025).

Metode diagnosis konvensional yang digunakan dalam dunia medis seringkali memerlukan waktu yang cukup lama, biaya yang tinggi, serta bergantung pada pengalaman tenaga medis. Oleh karena itu, diperlukan suatu pendekatan alternatif yang lebih cepat, efisien, dan akurat dalam membantu proses diagnosis penyakit diabetes. Salah satu pendekatan yang berkembang pesat adalah penggunaan teknologi machine learning dalam bidang kesehatan (Alzboon et al., 2025).

Machine learning merupakan cabang dari kecerdasan buatan yang memungkinkan sistem untuk belajar dari data dan membuat prediksi secara otomatis tanpa perlu diprogram secara eksplisit. Dalam konteks prediksi diabetes, machine learning digunakan untuk menganalisis data pasien seperti usia, indeks massa tubuh (BMI), tekanan darah, serta kadar glukosa dalam darah untuk menentukan kemungkinan seseorang menderita diabetes (Arsyad et al., 2024).

Berbagai algoritma machine learning telah digunakan dalam penelitian terkait klasifikasi diabetes, khususnya algoritma supervised learning. Di antara algoritma yang paling sering digunakan adalah Decision Tree (DT), Support Vector Machine (SVM), dan K-Nearest Neighbor (KNN). Ketiga algoritma ini memiliki pendekatan yang berbeda dalam melakukan klasifikasi data, sehingga menghasilkan performa yang bervariasi tergantung pada karakteristik dataset yang digunakan (Saleh et al., 2025).

Decision Tree merupakan algoritma yang bekerja dengan membentuk struktur pohon keputusan berdasarkan atribut data, sehingga mudah dipahami dan diinterpretasikan oleh pengguna. Algoritma ini banyak digunakan dalam bidang kesehatan karena mampu memberikan penjelasan yang jelas mengenai proses pengambilan keputusan (Tayyibah et al., 2025).

Di sisi lain, Support Vector Machine (SVM) merupakan algoritma yang bekerja dengan mencari hyperplane optimal untuk memisahkan data ke dalam dua kelas yang berbeda. Algoritma ini dikenal memiliki tingkat akurasi yang tinggi dan mampu menangani data berdimensi tinggi dengan baik. Beberapa penelitian menunjukkan bahwa SVM memiliki performa yang lebih unggul dibandingkan algoritma lainnya dalam klasifikasi diabetes (Adih et al., 2025).

Sementara itu, K-Nearest Neighbor (KNN) merupakan algoritma berbasis jarak yang mengklasifikasikan data berdasarkan kedekatan dengan data lain yang telah diketahui kelasnya. Algoritma ini memiliki keunggulan dalam kesederhanaan implementasi, namun memiliki kelemahan dalam hal efisiensi komputasi dan sensitivitas terhadap noise (Yunianto & Subhiyakto, 2025).

Berbagai penelitian terdahulu telah membandingkan performa ketiga algoritma tersebut dalam klasifikasi diabetes. Hasil penelitian menunjukkan bahwa algoritma SVM cenderung memiliki tingkat akurasi yang lebih tinggi dibandingkan algoritma lainnya, diikuti oleh Decision Tree dan KNN (Ardiansyah et al., 2024).

Namun, dalam beberapa penelitian lain, Decision Tree juga menunjukkan performa yang sangat baik setelah dilakukan optimasi parameter (Pratama, 2024). Selain itu, faktor seperti preprocessing data, pemilihan fitur, serta teknik balancing data juga memiliki pengaruh

<!-- End of 2 -->

<!--  Page 3  -->

JURNAL PENGANTAR KECERDASAN BUATAN,
VOL. 1 NO 1, April 2026, 1-11
yang signifikan terhadap performa model.
Teknik seperti SMOTE dan hyperparameter
tuning terbukti mampu meningkatkan akurasi
model secara signifikan (Yunianto &
Subhiyakto, 2025).
Berdasarkan latar belakang tersebut,
penelitian ini bertujuan untuk melakukan
kajian literatur mengenai perbandingan
algoritma Decision Tree, Support Vector
Machine, dan K-Nearest Neighbor dalam
klasifikasi prediksi diabetes. Penelitian ini
diharapkan dapat memberikan pemahaman
yang lebih mendalam mengenai kelebihan dan
kekurangan masing-masing algoritma serta
menjadi referensi dalam pemilihan metode
yang tepat untuk pengembangan sistem
prediksi diabetes di masa depan.
2. LITERATURE REVIEW
2.1 Machine Learning dalam Prediksi
Diabetes
Source: https://www.mdpi.com/785322
Machine learning merupakan cabang dari
kecerdasan buatan yang memungkinkan
sistem untuk belajar dari data dan
menghasilkan prediksi secara otomatis.
Dalam bidang kesehatan, penerapan machine
learning telah berkembang pesat, khususnya
dalam membantu diagnosis penyakit kronis
seperti diabetes mellitus.
Menurut penelitian yang dilakukan oleh
Alzboon et al. (2025), machine learning
mampu meningkatkan efisiensi dalam proses
diagnosis dengan menganalisis data medis
seperti kadar glukosa, BMI, tekanan darah,
serta faktor risiko lainnya. Dataset yang
digunakan dalam penelitian ini adalah
Pima Indians Diabetes Dataset,
yang dianggap representatif untuk kasus klasifikasi
diabetes.
Source: https://shonit2096.medium.com/classification-on-diabetes-data-set-
fe0d133d7821
Selain itu, penelitian oleh Saleh et al. (2025)
menunjukkan bahwa penggunaan algoritma
klasifikasi dalam machine learning dapat
menghasilkan tingkat akurasi yang tinggi dalam
prediksi diabetes, sehingga dapat digunakan
sebagai sistem pendukung keputusan dalam
bidang medis.
Penelitian lain juga menegaskan bahwa metode
klasifikasi merupakan pendekatan yang paling
efektif dalam mengelompokkan pasien ke dalam
kategori diabetes atau non-diabetes berdasarkan
data historis (Arsyad et al., 2024).
Dengan demikian, machine learning memiliki
peran penting dalam pengembangan sistem
diagnosis modern yang lebih cepat, akurat, dan
efisien.
2.2 Decision Tree dalam Prediksi Diabetes
Source: https://life-sciences-ml-at-
tacc.readthedocs.io/en/latest/section2/decision_tree_and_random_forest.html?
Decision Tree merupakan algoritma klasifikasi
yang bekerja dengan membentuk struktur pohon
keputusan berdasarkan atribut data. Algoritma
ini banyak digunakan dalam bidang kesehatan
karena memiliki tingkat interpretasi yang tinggi
dan mudah dipahami oleh pengguna.
Penelitian oleh Pratama (2024)
menunjukkan bahwa Decision Tree dapat

<!-- End of 3 -->

<!--  Page 4  -->

JURNAL PENGANTAR KECERDASAN BUATAN,
VOL. 1 NO 1, April 2026, 1-11

menghasilkan performa yang sangat tinggi
dalam prediksi diabetes, terutama setelah
dilakukan optimasi parameter menggunakan
GridSearchCV. Dalam penelitian tersebut,
akurasi model meningkat hingga mencapai
97,06%, yang menunjukkan bahwa optimasi
parameter memiliki pengaruh signifikan
terhadap performa model.

Information Gain (IG)
IG = Entropy (Parent) - weighted_avg * Entropy (Children)
Information gain for Age
Source: https://medium.com/data-science/decision-tree-part-2-34b31b1dc328

Selain itu, penelitian oleh Yunianto dan
Subhiyakto (2025) membandingkan Decision
Tree dengan KNN dan menunjukkan bahwa
Decision Tree memiliki performa yang lebih
stabil. Tanpa menggunakan teknik balancing
data, Decision Tree mencapai akurasi sebesar
85,71%, sedangkan KNN hanya mencapai
83,12%. Setelah menggunakan metode
SMOTE, akurasi Decision Tree meningkat
menjadi 92%, yang menunjukkan bahwa
algoritma ini cukup robust terhadap masalah
ketidakseimbangan data.

Penelitian lain oleh Dwinnie et al. (2024)
menunjukkan bahwa Decision Tree memiliki
akurasi sebesar 86% dalam klasifikasi
diabetes, yang setara dengan KNN namun
lebih unggul dalam hal interpretasi model.

Meskipun memiliki banyak keunggulan,
Decision Tree juga memiliki kelemahan yaitu
kecenderungan mengalami overfitting jika
tidak dilakukan pruning atau pengaturan
parameter yang tepat. Oleh karena itu,
penggunaan teknik optimasi sangat
diperlukan untuk meningkatkan performa
model.

2.3 Support Vector Machine (SVM) dalam
Prediksi Diabetes

Support Vector Machine (SVM) merupakan
algoritma klasifikasi yang bekerja dengan
mencari hyperplane optimal yang dapat
memisahkan data ke dalam dua kelas dengan
margin maksimum. Algoritma ini dikenal
memiliki performa yang sangat baik dalam
menangani data kompleks dan berdimensi tinggi.

Penelitian oleh Saleh et al. (2025)
menunjukkan bahwa SVM memiliki tingkat
akurasi tertinggi dibandingkan algoritma
lainnya, yaitu sebesar 94,5%. Hal ini
menunjukkan bahwa SVM sangat efektif dalam
mengidentifikasi pola dalam data medis.

Source: https://medium.com/@codethulo/rbf-kernels-2e8c4f2d8ea5

Selain itu, penelitian oleh (Adih et al.,
2025) yang merupakan literature review khusus
SVM menyatakan bahwa algoritma SVM secara
konsisten menghasilkan akurasi di atas 90% dan
lebih unggul dibandingkan metode lain seperti
Naïve Bayes dan Decision Tree dalam
klasifikasi diabetes.

Penelitian oleh Wafa et al. (2022) juga
menunjukkan bahwa SVM dengan kernel Radial
Basis Function (RBF) mampu mencapai akurasi
sebesar 91%, yang menunjukkan bahwa
pemilihan kernel sangat mempengaruhi
performa model.

Namun, penelitian oleh As’ari dan Kusrini
(2025) menunjukkan bahwa performa SVM juga
sangat dipengaruhi oleh preprocessing data.
Dalam penelitian tersebut, SVM dengan pipeline
preprocessing menghasilkan akurasi sebesar
76,6% dan nilai ROC AUC sebesar 0,861, yang


<!-- End of 4 -->

<!--  Page 5  -->

JURNAL PENGANTAR KECERDASAN BUATAN,
VOL. 1 NO 1, April 2026, 1-11
menunjukkan bahwa kualitas data memiliki
pengaruh signifikan terhadap hasil model.
Dengan demikian, dapat disimpulkan
bahwa SVM merupakan algoritma dengan
performa terbaik dalam prediksi diabetes,
namun memerlukan tuning parameter dan
preprocessing yang tepat untuk mencapai
hasil optimal.
2.4 K-Nearest Neighbor (KNN) dalam
Prediksi Diabetes
Source:https://medium.com@ sachinson600517/k-nearest-neighbours-
introduction-to-machine-learning-algorithms-9dbc9d9fb3b2
K-Nearest Neighbor (KNN) merupakan
algoritma klasifikasi berbasis jarak yang
menentukan kelas suatu data berdasarkan
mayoritas kelas dari tetangga terdekatnya.
Algoritma ini dikenal sederhana dan mudah
diimplementasikan.
Penelitian oleh Saleh et al. (2025) menunjukkan bahwa KNN memiliki performa
yang cukup baik dengan tingkat akurasi
sebesar 92,5%, meskipun masih berada di
bawah SVM.
Selain itu, penelitian oleh Yunianto dan
Subhiyakto (2025) menunjukkan bahwa KNN
memiliki akurasi sebesar 83,12% tanpa
preprocessing, dan meningkat menjadi 91%
setelah menggunakan teknik SMOTE, yang
menunjukkan bahwa performa KNN sangat
dipengaruhi oleh kualitas data.
Penelitian oleh Dwinnie et al. (2024) juga
menunjukkan bahwa KNN memiliki akurasi
sebesar 86%, yang menunjukkan bahwa
algoritma ini cukup kompetitif dalam klasifikasi
diabetes.
Namun, KNN memiliki beberapa kelemahan,
antara lain:
- Sensitif terhadap noise
- Lambat pada dataset besar
- Bergantung pada pemilihan parameter k
Meskipun demikian, KNN tetap menjadi
algoritma yang sering digunakan sebagai
baseline model dalam penelitian machine learning.
2.5 Sintesis Perbandingan Literatur
Berdasarkan seluruh penelitian yang telah dikaji,
dapat disimpulkan bahwa:
- SVM: unggul dalam akurasi dan performa
keseluruhan
- Decision Tree: unggul dalam interpretasi
dan stabilitas
- KNN: unggul dalam kesederhanaan
Selain itu, faktor seperti preprocessing data,
balancing data, dan hyperparameter tuning
memiliki pengaruh yang sangat besar terhadap
performa model.
Penelitian oleh Yunianto dan Subhiyakto (2025)
menunjukkan bahwa penggunaan SMOTE dapat
meningkatkan performa model secara signifikan,
sementara penelitian oleh Pratama (2024)
menunjukkan bahwa tuning parameter dapat
meningkatkan akurasi hingga lebih dari 97%.
3. RESEARCH METHOD
3.1 Jenis Penelitian
Penelitian ini menggunakan pendekatan
kualitatif deskriptif dengan metode literature
review, yaitu dengan mengkaji dan menganalisis
berbagai penelitian terdahulu yang berkaitan
dengan penerapan algoritma machine learning
dalam prediksi diabetes.

<!-- End of 5 -->

<!--  Page 6  -->

JURNAL PENGANTAR KECERDASAN BUATAN,
VOL. 1 NO 1, April 2026, 1-11

Metode literature review dipilih karena memungkinkan peneliti untuk memperoleh pemahaman yang komprehensif mengenai perkembangan algoritma klasifikasi serta membandingkan performa algoritma Decision Tree (DT), Support Vector Machine (SVM), dan K-Nearest Neighbor (KNN) berdasarkan hasil penelitian sebelumnya.

Pendekatan ini tidak melibatkan eksperimen langsung, melainkan berfokus pada analisis hasil penelitian yang telah dipublikasikan oleh peneliti lain (Adih et al., 2025).

\subsection*{3.2 Sumber Data dan Teknik Pengumpulan Data}

Data dalam penelitian ini berupa data sekunder, yaitu jurnal ilmiah nasional dan internasional yang relevan dengan topik prediksi diabetes menggunakan algoritma machine learning.

Kriteria pemilihan literatur meliputi:

1. Membahas algoritma klasifikasi (DT, SVM, KNN)
2. Menggunakan dataset diabetes
3. Menyediakan hasil evaluasi model (akurasi, precision, recall, F1-score)
4. Dipublikasikan dalam jurnal atau prosiding ilmiah

Sebagian besar penelitian menggunakan dataset standar seperti Pima Indians Diabetes Dataset, yang terdiri dari atribut medis seperti kadar glukosa, BMI, tekanan darah, dan usia pasien (Alzboon et al., 2025).

\subsection*{3.3 Tahapan Penelitian}

\begin{center}
\includegraphics[width=0.9\textwidth]{image.png}
\end{center}

Source: https://www.mdpi.com/2996214

Tahapan dalam penelitian ini meliputi:

1. Identifikasi Masalah
Menentukan topik penelitian terkait perbandingan algoritma machine learning dalam prediksi diabetes.

2. Pengumpulan Literatur
Mengumpulkan jurnal-jurnal ilmiah yang relevan dari berbagai sumber.

3. Seleksi Literatur
Memilih jurnal yang sesuai dengan kriteria penelitian.

4. Analisis Literatur
Membandingkan performa algoritma berdasarkan hasil penelitian terdahulu.

5. Sintesis Hasil
Menarik kesimpulan dari hasil perbandingan algoritma.

\subsection*{3.4 Algoritma yang Dianalisis}

Penelitian ini berfokus pada tiga algoritma klasifikasi, yaitu:

\subsubsection*{3.4.1 Decision Tree (DT)}

Decision Tree merupakan algoritma yang membentuk struktur pohon keputusan berdasarkan atribut data. Pemilihan atribut dilakukan menggunakan konsep entropy dan information gain.

\begin{equation}
Entropy(S) = -\sum_{i=1}^{n} p_i \log_2 p_i
\end{equation}

Entropy digunakan untuk mengukur tingkat ketidakpastian dalam dataset.

\begin{equation}
Gain(S, A) = Entropy(S) - \sum_{v \in Values(A)} \frac{|S_v|}{|S|} Entropy(S_v)
\end{equation}

Information gain digunakan untuk menentukan atribut terbaik dalam pemisahan data (Pratama, 2024).

\subsubsection*{3.4.2 Support Vector Machine (SVM)}

Support Vector Machine merupakan algoritma yang mencari hyperplane optimal untuk memisahkan data ke dalam dua kelas.

\begin{equation}
w \cdot x + b = 0
\end{equation}

Hyperplane ini digunakan sebagai batas keputusan antar kelas.

\begin{equation}
Margin = \frac{2}{|w|}
\end{equation}

Margin maksimum digunakan untuk meningkatkan generalisasi model (Adih et al., 2025).

\subsubsection*{3.4.3 K-Nearest Neighbor (KNN)}

<!-- End of 6 -->

<!--  Page 7  -->

JURNAL PENGANTAR KECERDASAN BUATAN,
VOL. 1 NO 1, April 2026, 1-11

K-Nearest Neighbor merupakan algoritma berbasis jarak yang mengklasifikasikan data berdasarkan kedekatan dengan tetangga terdekat.

$d(x,y) = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}$

Jarak Euclidean digunakan untuk menentukan kedekatan antar data (Yunianto & Subhiyakto, 2025)

3.5 Metode Evaluasi

Evaluasi performa algoritma dalam penelitian ini mengacu pada metrik yang digunakan dalam penelitian terdahulu, yaitu:

- Accuracy

$Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$

Mengukur tingkat keakuratan model secara keseluruhan.

- Precision

$Precision = \frac{TP}{TP + FP}$

Mengukur ketepatan prediksi positif.

- Recall

$Recall = \frac{TP}{TP + FN}$

Mengukur kemampuan model dalam mendeteksi data positif.

- F1-Score

$F1 = 2 \cdot \frac{Precision \cdot Recall}{Precision + Recall}$

Merupakan kombinasi antara precision dan recall.

3.6 Teknik Pendukung dalam Literatur

Berdasarkan berbagai penelitian yang dikaji, terdapat beberapa teknik yang berpengaruh terhadap performa model, antara lain:

- Preprocessing Data (normalisasi, cleaning data)
- Feature Selection
- Balancing Data menggunakan SMOTE
- Hyperparameter Tuning menggunakan GridSearchCV

Penelitian menunjukkan bahwa teknik-teknik tersebut mampu meningkatkan performa model secara signifikan, terutama pada Decision Tree dan KNN (Pratama, 2024; Yunianto & Subhiyakto, 2025)

3.7 Ringkasan Metodologi

Metodologi penelitian ini dirancang untuk melakukan analisis komparatif terhadap algoritma Decision Tree, Support Vector Machine, dan K-Nearest Neighbor berdasarkan hasil penelitian terdahulu.

Dengan pendekatan literature review, penelitian ini diharapkan mampu memberikan gambaran yang sistematis dan komprehensif mengenai performa masing-masing algoritma dalam prediksi diabetes.

4. DISCUSSION AND RESULT

4.1 Hasil Perbandingan Berdasarkan Literatur

Berdasarkan hasil kajian terhadap berbagai penelitian yang telah dianalisis, diperoleh bahwa algoritma Decision Tree (DT), Support Vector Machine (SVM), dan K-Nearest Neighbor (KNN) memiliki performa yang berbeda dalam klasifikasi prediksi diabetes. Perbedaan tersebut dipengaruhi oleh karakteristik dataset, teknik preprocessing, serta metode optimasi yang digunakan dalam masing-masing penelitian.

Penelitian oleh Saleh et al. (2025) menunjukkan bahwa algoritma SVM memiliki tingkat akurasi tertinggi yaitu sebesar 94,5%, diikuti oleh Decision Tree sebesar 93,5% dan KNN sebesar 92,5%. Hal ini menunjukkan bahwa SVM memiliki kemampuan yang lebih baik dalam mengklasifikasikan data diabetes dibandingkan algoritma lainnya.

Selain itu, penelitian oleh Ardiansyah et al. (2024) menunjukkan bahwa SVM dapat mencapai akurasi hingga 100% dalam kondisi tertentu. Meskipun demikian, hasil tersebut sangat bergantung pada kualitas data serta preprocessing yang digunakan.

Di sisi lain, penelitian oleh Pratama (2024) menunjukkan bahwa Decision Tree dapat mencapai akurasi sebesar 97,06% setelah dilakukan optimasi parameter menggunakan GridSearchCV. Hal ini menunjukkan bahwa performa algoritma Decision Tree dapat meningkat secara signifikan melalui teknik

<!-- End of 7 -->

<!--  Page 8  -->

JURNAL PENGANTAR KECERDASAN BUATAN,
VOL. 1 NO 1, April 2026, 1-11

tuning parameter.
Sementara itu, penelitian oleh Yunianto dan Subhiyakto (2025) menunjukkan bahwa Decision Tree memiliki performa yang lebih stabil dibandingkan KNN, baik sebelum maupun setelah penerapan teknik balancing data menggunakan SMOTE. Setelah menggunakan SMOTE, akurasi Decision Tree mencapai 92%, sedangkan KNN mencapai 91%.

## 4.2 Analisis Performa Support Vector Machine (SVM)

<!-- Image (115, 270, 475, 495) -->

Source: https://www.analyticsvidhya.com/blog/2020/10/the-mathematics-behind-svm/? 

Berdasarkan berbagai penelitian yang dikaji, Support Vector Machine (SVM) merupakan algoritma yang paling konsisten dalam menghasilkan performa tinggi dalam prediksi diabetes. Hal ini disebabkan oleh kemampuannya dalam membangun hyperplane optimal yang memaksimalkan margin antar kelas.

Penelitian oleh (Adih et al., 2025) menunjukkan bahwa SVM secara konsisten menghasilkan akurasi di atas 90% dan lebih unggul dibandingkan algoritma lain seperti Decision Tree dan Naïve Bayes.

Selain itu, penelitian oleh Wafa et al. (2022) menunjukkan bahwa penggunaan kernel Radial Basis Function (RBF) pada SVM mampu meningkatkan akurasi hingga 91%, yang menunjukkan bahwa pemilihan kernel memiliki pengaruh besar terhadap performa model.

Namun, penelitian oleh As’ari dan Kusroni (2025) menunjukkan bahwa performa SVM sangat dipengaruhi oleh preprocessing data. Dalam penelitian tersebut, SVM menghasilkan akurasi sebesar 76,6% dengan nilai ROC AUC sebesar 0,861 setelah melalui berbagai tahapan preprocessing.

Hal ini menunjukkan bahwa meskipun SVM memiliki potensi performa tinggi, hasil akhirnya tetap bergantung pada kualitas data dan proses preprocessing yang digunakan.

## 4.3 Analisis Performa Decision Tree (DT)

<!-- Image (515, 230, 898, 355) -->

Source: https://medium.com/@merohit2004raj/decision-tree-in-machine-learning-7f7e7bddfcfb

Decision Tree menunjukkan performa yang sangat baik dalam berbagai penelitian, terutama dalam hal stabilitas dan interpretasi model.

Penelitian oleh Pratama (2024) menunjukkan bahwa Decision Tree dapat mencapai akurasi sebesar 97,06% setelah dilakukan optimasi parameter menggunakan GridSearchCV. Hal ini menunjukkan bahwa algoritma ini memiliki potensi performa yang sangat tinggi jika dikombinasikan dengan teknik tuning yang tepat.

Selain itu, penelitian oleh Yunianto dan Subhiyakto (2025) menunjukkan bahwa Decision Tree memiliki performa yang lebih stabil dibandingkan KNN, terutama dalam kondisi dataset yang tidak seimbang.

Penelitian oleh Dwinnie et al. (2024) juga menunjukkan bahwa Decision Tree memiliki akurasi sebesar 86%, yang menunjukkan bahwa algoritma ini cukup kompetitif dalam klasifikasi diabetes.

Keunggulan utama Decision Tree adalah kemampuannya dalam menghasilkan model yang mudah dipahami, sehingga sangat cocok digunakan dalam bidang kesehatan. Namun, kelemahan utama algoritma ini adalah kecenderungan mengalami overfitting jika tidak dilakukan pruning.

## 4.4 Analisis Performa K-Nearest Neighbor (KNN)

<!-- End of 8 -->

<!--  Page 9  -->

JURNAL PENGANTAR KECERDASAN BUATAN,
VOL. 1 NO 1, April 2026, 1-11

Eucidean distance (d) = $\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$

Source: https://www.analyticsvidhya.com/blog/2015/08/learning-
concept-knn-algorithms-programming/

K-Nearest Neighbor (KNN) merupakan
algoritma yang paling sederhana
dibandingkan DT dan SVM. Algoritma ini
tidak memerlukan proses training yang
kompleks, sehingga mudah diimplementasikan.

Penelitian oleh Saleh et al. (2025) menunjukkan bahwa KNN memiliki akurasi sebesar 92,5%, yang menunjukkan bahwa
algoritma ini cukup kompetitif dalam
klasifikasi diabetes.

Namun, penelitian oleh Yunianto dan
Subhiyakto (2025) menunjukkan bahwa KNN memiliki performa yang lebih rendah dibandingkan Decision Tree, terutama pada dataset besar.

Selain itu, penelitian oleh Dwnnie et al.
(2024) menunjukkan bahwa KNN memiliki akurasi sebesar 86%, yang setara dengan Decision Tree namun lebih rendah dalam hal stabilitas performa.

Kelemahan utama KNN adalah:
- Sensitif terhadap noise
- Lambat pada dataset besar
- Bergantung pada parameter k

4.5 Pengaruh Preprocessing terhadap
Performa Model

Salah satu temuan penting dari berbagai
penelitian adalah penelitian bahwa preprocessing data memiliki pengaruh yang sangat besar terhadap performa model.

Penelitian oleh Yunianto dan Subhiyakto
(2025) menunjukkan bahwa penggunaan SMOTE dapat meningkatkan akurasi model secara signifikan, terutama pada dataset yang tidak seimbang.

Selain itu, penelitian oleh Pratama (2024) menunjukkan bahwa penggunaan hyperparameter tuning seperti GridSearchCV dapat meningkatkan akurasi model hingga lebih dari 97%.

Hal ini menunjukkan bahwa keberhasilan model tidak hanya ditentukan oleh algoritma yang digunakan, tetapi juga oleh kualitas data dan teknik preprocessing yang diterapkan.

4.6 Sintesis dan Implikasi

Berdasarkan hasil analisis yang telah
dilakukan, dapat disimpulkan bahwa:
1. SVM merupakan algoritma terbaik
dalam hal akurasi
2. Decision Tree unggul dalam interpretasi
dan stabilitas
3. KNN unggul dalam kesederhanaan
namun memiliki keterbatasan

Implikasi dari penelitian ini adalah bahwa pemilihan algoritma harus disesuaikan dengan kebutuhan sistem:
- Sistem berbasis akurasi tinggi: SVM
- Sistem berbasis interpretasi: Decision
Tree
- Sistem sederhana: KNN

4.7 Ringkasan Hasil

Secara keseluruhan, tidak terdapat satu
algoritma yang secara mutlak unggul dalam semua kondisi. Kombinasi antara algoritma yang tepat, preprocessing data, serta optimasi parameter merupakan faktor utama dalam menghasilkan model prediksi yang optimal.

5. KESIMPULAN

Berdasarkan hasil kajian literatur yang telah
dilakukan terhadap berbagai penelitian terkait
penggunaan algoritma machine learning dalam
prediksi diabetes, dapat disimpulkan bahwa
algoritma Decision Tree (DT), Support Vector
Machine (SVM), dan K-Nearest Neighbor
(KNN) memiliki karakteristik, keunggulan, serta
keterbatasan masing-masing dalam proses
klasifikasi data medis.

Support Vector Machine (SVM) secara
umum menunjukkan performa terbaik dalam hal
akurasi dibandingkan algoritma lainnya. Hal ini
didukung oleh berbagai penelitian yang
menunjukkan bahwa SVM mampu mencapai
tingkat akurasi di atas 90%, bahkan dalam

<!-- End of 9 -->

<!--  Page 10  -->

JURNAL PENGANTAR KECERDASAN BUATAN,
VOL. 1 NO 1, April 2026, 1-11
beberapa kasus mencapai hingga 94,5% atau
lebih (Saleh et al., 2025; Adih et al., 2025).
Selain itu, penggunaan kernel seperti Radial
Basis Function (RBF) juga terbukti mampu
meningkatkan performa model dalam
menangani data non-linear (Wafa et al.,
2022).
Di sisi lain, Decision Tree menunjukkan
performa yang sangat baik dalam hal
stabilitas serta interpretasi model. Struktur
pohon keputusan yang dihasilkan
memungkinkan pengguna untuk memahami
proses pengambilan keputusan secara
transparan. Selain itu, penelitian
menunjukkan bahwa performa Decision Tree
dapat ditingkatkan secara signifikan melalui
teknik optimasi parameter seperti
GridSearchCV, dengan akurasi mencapai
97,06% (Pratama, 2024).
Sementara itu, K-Nearest Neighbor
(KNN) merupakan algoritma yang paling
sederhana dan mudah diimplementasikan.
Meskipun memiliki performa yang cukup
baik dengan akurasi yang kompetitif,
algoritma ini memiliki keterbatasan dalam hal
efisiensi komputasi pada dataset besar serta
sensitivitas terhadap noise dan pemilihan
parameter k (Yunianto & Subhiyakto, 2025).
Selain perbedaan performa antar
algoritma, hasil kajian juga menunjukkan
bahwa faktor lain seperti preprocessing data,
balancing data menggunakan metode
SMOTE, serta optimasi parameter memiliki
pengaruh yang sangat signifikan terhadap
performa model. Hal ini menunjukkan bahwa
keberhasilan model tidak hanya ditentukan
oleh algoritma yang digunakan, tetapi juga
oleh kualitas data dan teknik yang diterapkan
dalam proses pengolahan data.
Dengan demikian, dapat disimpulkan
bahwa tidak terdapat satu algoritma yang
secara mutlak unggul dalam semua kondisi.
Pemilihan algoritma yang tepat harus
disesuaikan dengan kebutuhan sistem serta
karakteristik data yang digunakan.
Secara praktis, apabila tujuan utama
adalah memperoleh tingkat akurasi yang
tinggi, maka algoritma Support Vector
Machine (SVM) merupakan pilihan yang
paling tepat. Namun, jika dibutuhkan model
yang mudah dipahami dan dapat dijelaskan,
maka Decision Tree menjadi alternatif yang
lebih sesuai. Sementara itu, K-Nearest Neighbor
(KNN) dapat digunakan sebagai solusi
sederhana dalam implementasi awal atau
sebagai pembanding dalam penelitian.
Penelitian ini diharapkan dapat memberikan
kontribusi dalam pengembangan sistem prediksi
diabetes berbasis machine learning yang lebih
akurat, efisien, dan aplikatif, serta menjadi
referensi bagi penelitian selanjutnya dalam
bidang kecerdasan buatan di sektor kesehatan.
6. DAFTAR PUSTAKA
Saleh, A., Sari, R. E., Ramadani, R., Fujtati,
F., & Lestari, R. (2025). Analisis komparatif
algoritma klasifikasi machine learning untuk
memprediksi diabetes. Jurnal Algoritma, 9(1),
26-35.
Alzboon, M. S., Alqaraleh, M., Al-Batah,
M., & Abuashour, A. (2025). A comparative
study of machine learning techniques for early
prediction of diabetes.
Vaishnavi, V., Jha, R., & Mitra, S. (2025).
Comparative study on prediction of diabetes
disease using machine learning models.
Tayyibah, H. Z., et al. (2025). Sistem
pendukung keputusan klasifikasi diabetes
menggunakan decision tree.
Kowsher, M., Turaba, M. Y., Rahman, M.
M., & Sajed, T. (2019). Prognosis and treatment
prediction of type-2 diabetes using machine
learning classifiers.
Arsyad, M. I., Amran, A., Desiani, A., &
Napitu, M. J. (2024). Comparison of classification
results of SVM, KNN, and decision tree.
Ardiansyah, A., Telaumbanua, E. C. O.,
Gultom, A. S., & Limbong, A. A. S. M. (2024).
Klasifikasi diabetes menggunakan SVM dan
KNN.
Adih, A., Pangestu, W. A. D., Akbar, M. F.,
Purnamasari, P., Wabula, F., & Ikasari, I. H.
(2025). Literature review penggunaan SVM untuk
klasifikasi diabetes.
Sutrisno, S., & Jupron, J. (2024). Analisa
klasifikasi diabetes dengan neural network.
Pratama, E. C. (2024). Optimasi algoritma
decision tree dalam prediksi diabetes
menggunakan GridSearchCV.
10

<!-- End of 10 -->

<!--  Page 11  -->

JURNAL PENGANTAR KECERDASAN BUATAN,
VOL. 1 NO 1, April 2026, 1-11

As’ari, H., & Kusmini, K. (2025). Peningkatan kinerja klasifikasi diabetes menggunakan SVM dengan kernel RBF.
Yunianto, A. H., & Subhiyakto, E. R. (2025). Perbandingan kinerja KNN dan decision tree untuk klasifikasi diabetes.
Dwinnie, Z. C., Dwyne, Z. C., Islam, M. J., & Noviarni, N. (2024). Comparison of machine learning algorithms in diabetes classification.
Nandaa, I. M. P. S., & Suputra, I. P. G. H. (2024). Perbandingan neural network, KNN, dan decision tree dalam klasifikasi diabetes.
Gunawan, S., Astuti, R., Priharto, W., & Hamonangan, R. (2025). Prediksi diabetes menggunakan logistic regression.
Wafa, H. S., Hadiana, A. I., & Umbara, F. R. (2022). Prediksi diabetes menggunakan algoritma SVM.

<!-- End of 11 -->

