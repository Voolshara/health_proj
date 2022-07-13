<template>
  <div class="container-form">
    <Dialog />
    <p class="main-par">Анкета 1</p>
    <p class="sub_information" style="font-size: 20px">
      С вами на связи всегда будет личный помощник (ваш личный врач). Задавайте
      ему любые вопросы, поручайте дела и просто общайтесь в любое удобное для
      вас время/ мы с вами 24/7. Заполнение каждой анкеты действительно до 3х
      дней.
    </p>
    <el-divider />

    <div v-if="status_of_form == 4" class="form-send">Форма отправлена</div>

    <div v-else>
      <div v-if="status_of_form == 0">
        <el-upload
          class="avatar-uploader"
          action="http://localhost:5000/upload_avatar"
          :show-file-list="false"
          :on-success="handleAvatarSuccess"
          :before-upload="beforeAvatarUpload"
        >
          <img v-if="imageUrl" :src="imageUrl" class="avatar" />
          <el-icon v-else class="avatar-uploader-icon"><Plus /></el-icon>
        </el-upload>
        <p>Вам необходимо отправить нам фото 6x5;</p>
      </div>
      <el-form
        :model="form"
        label-width="300px"
        class="form"
        :label-position="'top'"
      >
        <div v-if="status_of_form == 1" class="form-send">
          <el-form-item label="Соблюдаете ли вы диету?">
            <el-radio-group v-model="form.diete">
              <el-radio :label="true" size="large" border>Да</el-radio>
              <el-radio :label="false" size="large" border>Нет</el-radio>
            </el-radio-group>
          </el-form-item>

          <div
            style="
              box-shadow: var(--el-box-shadow-lighter);
              padding: 10px;
              margin: 10px;
            "
          >
            <el-form-item label="Использовали ли вы ботулинотерапию?">
              <el-radio-group v-model="form.boutuline">
                <el-radio :label="true" size="large" border>Да</el-radio>
                <el-radio :label="false" size="large" border>Нет</el-radio>
              </el-radio-group>
            </el-form-item>

            <el-form-item label="Куда именно?" v-if="form.boutuline">
              <el-input
                v-model="form.where_boutuline"
                placeholder="Укажите место"
              />
              <div style="text-align: left">
                <p style="font-size: 20px; margin-top: 15px">
                  Функции ботулинотерапии
                </p>
                <p>1.Эффект длится в течении до 3 месяце;</p>
                <p>
                  2.Прописывается далеко не всем / если нет самого движения , то
                  делать его необходимости нет;
                </p>
                <p>3.Очень болезненно;</p>
                <p>4.Ботулинотерапия вводится не всегда в правильные места;</p>
                <p>
                  5.Расслабляет спазмированные мышцы, но замедляет работу
                  импульсов.
                </p>
              </div>
            </el-form-item>
          </div>

          <el-form-item label="Имеется ли у вас депрессия?">
            <el-radio-group v-model="form.depression">
              <el-radio :label="true" size="large" border>Да</el-radio>
              <el-radio :label="false" size="large" border>Нет</el-radio>
            </el-radio-group>
          </el-form-item>

          <el-form-item label="Были ли у вас судороги?">
            <el-radio-group v-model="form.sudoroga">
              <el-radio :label="true" size="large" border>Да</el-radio>
              <el-radio :label="false" size="large" border>Нет</el-radio>
            </el-radio-group>
          </el-form-item>

          <div
            style="
              box-shadow: var(--el-box-shadow-lighter);
              padding: 10px;
              margin: 10px;
            "
          >
            <el-form-item label="Нарушена ли у вас терморегуляция?">
              <el-radio-group v-model="form.termo">
                <el-radio :label="true" size="large" border>Да</el-radio>
                <el-radio :label="false" size="large" border>Нет</el-radio>
              </el-radio-group>
            </el-form-item>

            <el-form-item v-if="form.termo">
              <el-checkbox-group v-model="form.what_termo">
                <div style="display: flex; flex-direction: column">
                  <el-checkbox label="Холод" name="type" />
                  <el-checkbox label="Жар" name="type" />
                </div>
              </el-checkbox-group>
            </el-form-item>

            <el-form-item label="В каком именно месте?" v-if="form.termo">
              <el-input
                v-model="form.where_termo"
                placeholder="Укажите место"
              />
            </el-form-item>
          </div>

          <div
            style="
              box-shadow: var(--el-box-shadow-lighter);
              padding: 10px;
              margin: 10px;
            "
          >
            <el-form-item label="Имеется ли у вас головокружение?">
              <el-radio-group v-model="form.headache">
                <el-radio :label="true" size="large" border>Да</el-radio>
                <el-radio :label="false" size="large" border>Нет</el-radio>
              </el-radio-group>
            </el-form-item>

            <el-form-item
              label="Укажите уровень головокружения"
              v-if="form.headache"
            >
              <el-select
                v-model="form.lvl_of_headache"
                placeholder="Укажите уровень"
              >
                <el-option label="1" value="1" />
                <el-option label="2" value="2" />
                <el-option label="3" value="3" />
                <el-option label="4" value="4" />
                <el-option label="5" value="5" />
              </el-select>
            </el-form-item>
          </div>

          <el-form-item label="Имеется ли у вас страх от падений?">
            <el-radio-group v-model="form.fear_of_high">
              <el-radio :label="true" size="large" border>Да</el-radio>
              <el-radio :label="false" size="large" border>Нет</el-radio>
            </el-radio-group>
          </el-form-item>

          <el-form-item v-if="form.fear_of_high"
            ><p style="line-height: 15px; text-align: left; font-size: 15px">
              Если повредится\сломается неработающая больная сторона - то она
              срастается очень медленно. Поэтому лучше защититься заранее
            </p>
          </el-form-item>
        </div>

        <div v-else-if="status_of_form == 2">
          <el-form-item>
            <p style="font-size: 40px; margin: auto">ПОВРЕЖДЕНИЯ</p>
            <p style="font-size: 15px; margin-top: 15px">
              Из-за промедления времени с восстановлением вся поврежденная
              сторона опускается вниз и начинаются различные боли в разных
              частях тела
            </p>
          </el-form-item>

          <div
            style="
              box-shadow: var(--el-box-shadow-lighter);
              padding: 10px;
              margin: 10px;
            "
          >
            <el-form-item label="Имеется ли у вас боль?">
              <el-radio-group v-model="form.pain">
                <el-radio :label="true" size="large" border>Да</el-radio>
                <el-radio :label="false" size="large" border>Нет</el-radio>
              </el-radio-group>
            </el-form-item>
            <el-form-item v-if="form.pain"
              >Укажите место боли и рядом опишите её</el-form-item
            >
            <el-form-item label="1" v-if="form.pain">
              <el-input v-model="form.pain1" placeholder="Опишите боль" />
            </el-form-item>
            <el-form-item label="2" v-if="form.pain">
              <el-input v-model="form.pain2" placeholder="Опишите боль" />
            </el-form-item>
            <el-form-item label="3" v-if="form.pain">
              <el-input v-model="form.pain3" placeholder="Опишите боль" />
            </el-form-item>
          </div>
          <!-- <el-form-item>
            <el-carousel :interval="4000" type="card" height="200px">
              <el-carousel-item v-for="item in 6" :key="item">
                <h3 text="2xl" justify="center">{{ item }}</h3>
              </el-carousel-item>
            </el-carousel>
          </el-form-item> -->

          <el-form-item label="Пострадала ли у вас мимика?">
            <el-radio-group v-model="form.mimika">
              <el-radio :label="true" size="large" border>Да</el-radio>
              <el-radio :label="false" size="large" border>Нет</el-radio>
            </el-radio-group>
          </el-form-item>

          <div
            style="
              box-shadow: var(--el-box-shadow-lighter);
              padding: 10px;
              margin: 10px;
            "
          >
            <el-form-item label="Имеется ли у вас спастика?">
              <el-radio-group v-model="form.spastika">
                <el-radio :label="true" size="large" border>Да</el-radio>
                <el-radio :label="false" size="large" border>Нет</el-radio>
              </el-radio-group>
            </el-form-item>

            <el-form-item v-if="form.spastika">
              <el-checkbox-group v-model="form.type_of_spastika">
                <div style="display: flex; flex-direction: column">
                  <el-checkbox label="Рука" name="type" />
                  <el-checkbox label="Нога" name="type" />
                  <el-checkbox label="Другое" name="type" />
                </div>
              </el-checkbox-group>
            </el-form-item>
          </div>

          <div
            style="
              box-shadow: var(--el-box-shadow-lighter);
              padding: 10px;
              margin: 10px;
            "
          >
            <el-form-item label="Имеется ли у вас тонус?">
              <el-radio-group v-model="form.tonus">
                <el-radio :label="true" size="large" border>Да</el-radio>
                <el-radio :label="false" size="large" border>Нет</el-radio>
              </el-radio-group>
            </el-form-item>
            <el-form-item label="Где именно?" v-if="form.tonus">
              <el-input v-model="form.where_tonus" placeholder="" />
            </el-form-item>
          </div>
        </div>

        <div v-else-if="status_of_form == 0">
          <el-form-item label="Ваш рост (см)">
            <el-input-number
              v-model="form.growth"
              :controls="false"
              placeholder="Укажите число в см"
              size="large"
            />
          </el-form-item>

          <el-form-item label="Ваш вес (кг)">
            <el-input-number
              v-model="form.weight"
              :controls="false"
              placeholder="Укажите число в см"
              size="large"
            />
          </el-form-item>

          <el-form-item label="Ваш город">
            <el-input v-model="form.city" placeholder="Укажите город" />
          </el-form-item>

          <el-form-item label="Имеется ли у вас сопутствующие заболевания?">
            <el-radio-group v-model="form.is_illy">
              <el-radio :label="true" size="large" border>Да</el-radio>
              <el-radio :label="false" size="large" border>Нет</el-radio>
            </el-radio-group>
          </el-form-item>

          <el-form-item label="Принимаете ли вы лекарства?">
            <el-radio-group v-model="form.is_use_treatments">
              <el-radio :label="true" size="large" border>Да</el-radio>
              <el-radio :label="false" size="large" border>Нет</el-radio>
            </el-radio-group>
          </el-form-item>

          <el-form-item label="Какие?" v-if="form.is_use_treatments">
            <el-input v-model="form.what_treatments" placeholder="Фамилия" />
          </el-form-item>

          <el-form-item
            label="Владеете ли вы какой-либо информацией о инсульте?"
          >
            <el-radio-group v-model="form.know_some_information">
              <el-radio :label="true" size="large" border>Да</el-radio>
              <el-radio :label="false" size="large" border>Нет</el-radio>
            </el-radio-group>
          </el-form-item>

          <el-form-item label="Была ли у вас реабилитация?">
            <el-radio-group v-model="form.reabilitation">
              <el-radio :label="true" size="large" border>Да</el-radio>
              <el-radio :label="false" size="large" border>Нет</el-radio>
            </el-radio-group>
          </el-form-item>

          <el-form-item
            label="Что именно вы выполняли?"
            v-if="form.reabilitation"
          >
            <el-checkbox-group v-model="form.what_reabilitation">
              <div style="display: flex; flex-direction: column">
                <el-checkbox label="Массаж" name="type" />
                <el-checkbox label="Иглоукалывание" name="type" />
                <el-checkbox label="Физио-терапия" name="type" />
                <el-checkbox label="Аква терапия" name="type" />
                <el-checkbox label="Пиллатес" name="type" />
                <el-checkbox label="Эрготерапия" name="type" />
                <el-checkbox label="Гимнастика" name="type" />
                <el-checkbox label="Электростимуляция" name="type" />
                <el-checkbox label="Другое" name="type" />
              </div>
            </el-checkbox-group>
          </el-form-item>
        </div>

        <w8_form v-if="status_of_form == 3" @value="write_session" />
        <el-form-item v-if="status_of_form < 3">
          <el-button type="primary" @click="onSubmit">Продолжить</el-button>
        </el-form-item>
        <el-form-item v-else>
          <el-button type="primary" @click="onSubmit"
            >Отправить запрос на восстановление</el-button
          >
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import Dialog from "@/components/dialog.vue";
import w8_form from "@/components/next_session.vue";
export default {
  name: "FormFirst",
  components: {
    Dialog,
    w8_form,
  },
  data() {
    return {
      imageUrl: "/img/file_add.png",
      next_session: 0,
      form: {
        growth: "",
        weight: "",
        city: "",
        is_illy: "",
        is_use_treatments: "",
        what_treatments: "",
        know_some_information: "",
        reabilitation: "",
        what_reabilitation: [],
        diete: "",
        boutuline: "",
        where_boutuline: "",
        depression: "",
        sudoroga: "",
        termo: "",
        what_termo: [],
        where_termo: "",
        headache: "",
        lvl_of_headache: "",
        fear_of_high: "",
        pain: "",
        pain1: "",
        pain2: "",
        pain3: "",
        mimika: "",
        spastika: "",
        type_of_spastika: [],
        tonus: "",
        where_tonus: "",
      },
      status_of_form: 0,
    };
  },
  methods: {
    onSubmit: function () {
      this.status_of_form += 1;
      if (this.status_of_form == 4) {
        // fetch("http://localhost:5600/form1", {
        let data = this.form;
        data["next_session"] = this.next_session;
        fetch("http://localhost:5600/form1", {
          method: "POST", // *GET, POST, PUT, DELETE, etc.
          mode: "cors", // no-cors, *cors, same-origin
          cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
          credentials: "same-origin", // include, *same-origin, omit
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Private-Network": true,
          },
          redirect: "follow", // manual, *follow, error
          referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
          body: JSON.stringify({
            data: data,
          }), // body data type must match "Content-Type" header
        })
          .then((response) => response.json())
          .then((data) => {
            (this.form_is_send = true), console.log(data);
          })
          .catch((error) => {
            console.error("Error:", error);
            return null;
          });
      }
    },
    write_session(val) {
      this.next_session = val;
    },
  },
};
</script>

<style scoped>
.avatar-uploader .avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>

<style>
.avatar-uploader .el-upload {
  border: 1px dashed var(--el-border-color);
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: var(--el-transition-duration-fast);
}

.avatar-uploader .el-upload:hover {
  border-color: var(--el-color-primary);
}

.el-icon.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  text-align: center;
}
.container-form {
  align-items: center;
  text-align: center;
}

.sub_information {
  width: 70vw;
  margin: auto;
  margin-bottom: 15px;
}

.form {
  position: relative;
  align-self: center;
  padding: 0 3vw 0 0;
  width: 40vw;
  margin: auto;
  margin-top: 50px;
}

.main-par {
  color: #0836b5;
  background-image: url("@/assets/bg_header.png");
  font-style: normal;
  font-weight: 900;
  font-size: 70px;
  line-height: 145px;
}
</style>
