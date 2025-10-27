## 📊 Pixela Tracker 

Bu Python projesi, **[Pixela API](https://pixe.la/)** üzerinden günlük çalışma (veya başka bir aktivite) süreni takip etmeni sağlar.
Kullanıcı oluşturabilir, grafik ekleyebilir, günlük verilerini girebilir, güncelleyebilir veya silebilirsin.

---

### 🚀 Özellikler

* ✅ Pixela hesabı oluşturma
* 📈 Grafik (Graph) oluşturma
* 🟣 Günlük çalışma süresini ekleme (Pixel ekleme)
* ✏️ Mevcut günü güncelleme
* ❌ Günlük veriyi silme

---

### 🧰 Gereksinimler

* Python 3.7+
* `requests` modülü

Yüklemek için:

```bash
pip install requests
```

---

### ⚙️ Kullanım

1. **Kodda kullanıcı bilgilerini düzenle:**

```python
USERNAME = "ecemnurozen"
TOKEN = "1234567890ecemnurozen"
GRAPH_ID = "graph1"
```

2. **Kullanıcı hesabı oluşturmak için:**

```python
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
```

3. **Grafik oluşturmak için:**

```python
response_graph = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response_graph.text)
```

4. **Günlük çalışma süresi eklemek için:**

```python
response_create_pixel = requests.post(url=f"{graph_endpoint}/{GRAPH_ID}", json=pixel, headers=headers)
print(response_create_pixel.text)
```

5. **Veriyi güncellemek için:**

```python
response_update_pixel = requests.put(url=f"{graph_endpoint}/{GRAPH_ID}/{today.strftime('%Y%m%d')}", json=update_pixel, headers=headers)
print(response_update_pixel.text)
```

6. **Veriyi silmek için:**

```python
response_delete_pixel = requests.delete(url=delete_endpoint, headers=headers)
print(response_delete_pixel.text)
```

---

### 📅 Örnek Akış

```bash
$ python main.py
How many hours did you study today? 3.5
{"message":"Success.","isSuccess":true}
```

---

### 🧩 Notlar

* `TOKEN` değerini güvenli bir şekilde sakla (örneğin `.env` dosyasında).
* Pixela, tarih formatını `YYYYMMDD` olarak ister (örnek: `20251027`).
* `color` parametresinde şu değerler kullanılabilir: `shibafu`, `momiji`, `sora`, `ichou`, `ajisai`, `kuro`.

---

### 📘 Kaynaklar

* 📖 Pixela Resmi Dokümantasyonu: [https://docs.pixe.la/](https://docs.pixe.la/)
* 💡 API endpoint: `https://pixe.la/v1/users`
